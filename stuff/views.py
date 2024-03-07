from django.db.models import Prefetch
from django.http import JsonResponse
from django.views import View
import base64
import json

from builds.models import BuildModel
from stuff.models import Companion, MainRune, Skill, SubRune


class GetBuildInfo(View):
    def get(self, request, build_id):
        try:
            build = BuildModel.objects.get(pk=build_id)
        except BuildModel.DoesNotExist:
            return JsonResponse({"error": "Build does not exist"})
        return self.build_response(build)

    def build_response(self, build):
        decoded_collection_string = base64.b64decode(build.build_string).decode('utf-8')
        _, equipment_string = decoded_collection_string.split('|')

        equipment_data = json.loads(equipment_string)

        companions_list = self._get_equipment_info(equipment_data['companionsList'], Companion)
        skill_list = self._get_equipment_info(equipment_data['skillList'], Skill)
        main_rune_list = self._get_equipment_info(equipment_data['mainRuneList'], MainRune)
        sub_rune_list = self._get_equipment_info(equipment_data['subRuneList'], SubRune)

        mp, maxMp = self.calculate_mp(companions_list, sub_rune_list)

        response_data = {
            'companions': companions_list,
            'skills': skill_list,
            'mainRunes': main_rune_list,
            'subRunes': sub_rune_list,
            'mp': mp,
            'maxMp': maxMp
        }

        return JsonResponse(response_data)

    def calculate_mp(self, companions_list, sub_rune_list):
        max_mp = 30

        companion_slugs = [companion['slug'] for companion in companions_list if companion != {}]
        companions = Companion.objects.filter(slug__in=companion_slugs).prefetch_related('types')

        detailed_companion_list = {}
        for companion in companions:
            base_mp_adjustment = 0
            companion_level = next((item['level'] for item in companions_list if item['slug'] == companion.slug), None)

            if companion.slug in ['lulu', 'jack-striker'] and companion_level is not None:
                if companion_level >= 111:
                    base_mp_adjustment = 3
                elif companion_level >= 71:
                    base_mp_adjustment = 2
                elif companion_level >= 31:
                    base_mp_adjustment = 1
                else:
                    base_mp_adjustment = 0
            else:
                base_mp_adjustment = 0

            detailed_companion_list[companion.slug] = {
                "types": [type_obj.slug for type_obj in companion.types.all()],
                "rarity": companion.rarity,
                "mp_cost": companion.base_mp - base_mp_adjustment
            }

        sub_runes_conditions = [{'slug': sub_rune['slug'], 'rarity': sub_rune['rarity']} for sub_rune in sub_rune_list if sub_rune != {}]
        sub_runes = SubRune.objects.none()

        for condition in sub_runes_conditions:
            sub_runes |= SubRune.objects.filter(**condition)

        sub_runes = [SubRune.objects.get(slug="animal-mp-improved", rarity="legendary"),  # to remove
                     SubRune.objects.get(slug="max-mp-increased", rarity="legendary"),  # to remove
                     ]  # to remove

        for sub_rune in sub_runes:
            if sub_rune.type.name == "increase_max_mp":
                max_mp += int(sub_rune.values[0])
            elif sub_rune.type.name == "reduce_mp_for_companion_type_and_rarity":
                mp_reduction, companion_type, rarity = sub_rune.values
                for companion, data in detailed_companion_list.items():
                    if companion_type in data["types"]:
                        if rarity == "all" or rarity == data["rarity"]:
                            detailed_companion_list[companion]["mp_cost"] -= int(mp_reduction)
        total_mp_cost = sum(data["mp_cost"] for data in detailed_companion_list.values())
        return(total_mp_cost, max_mp)

    def _get_equipment_info(self, equipment_list, model):
        result = []
        for equipment in equipment_list:
            if 'id' in equipment:
                if model == MainRune:  # to remove
                    equipment_id = equipment['id'] - 111  # to remove
                else:  # to remove
                    equipment_id = equipment['id']  # to remove
                try:
                    item = model.objects.get(id=equipment_id)
                    data = {'slug': item.slug, 'rarity': item.rarity}
                    if 'level' in equipment:
                        data["level"] = equipment["level"]
                    result.append(data)
                except model.DoesNotExist:
                    result.append({'error': 'Item not found'})
            else:
                result.append({})
        return result
