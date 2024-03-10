import base64
import json
from stuff.models import Companion, MainRune, Skill, SubRune


def return_all_data():
    companions = Companion.objects.prefetch_related('types').distinct().values(
        'id', 'name', 'slug', 'rarity', 'base_mp').order_by("id")
    skills = Skill.objects.prefetch_related('types').values(
        'id', 'name', 'slug', 'rarity', 'description', 'cooldown').order_by("id")
    mainRunes = MainRune.objects.values('id', 'name', 'slug', 'rarity', 'description').order_by("id")
    subRunes = SubRune.objects.select_related('type').values(
        'id', 'name', 'slug', 'rarity', 'description', 'type__name', 'values').order_by("id")

    companions_data = [
        {**companion, 'types': [type_.slug for type_ in Companion.objects.get(id=companion['id']).types.all()]}
        for companion in companions
    ]

    skills_data = [
        {**skill, 'types': [type_.slug for type_ in Skill.objects.get(id=skill['id']).types.all()]}
        for skill in skills
    ]

    response_data = {
        'companions': companions_data,
        'skills': skills_data,
        'mainRunes': list(mainRunes),
        'subRunes': list(subRunes),
        'rarities': ["common", "uncommon", "rare", "epic", "legendary", "mythic"],
    }

    return response_data


def calculate_mp(companions_list, sub_rune_list, maxMp):
    companion_slugs = [companion['slug'] for companion in companions_list if companion != {}]
    companions = Companion.objects.filter(slug__in=companion_slugs).prefetch_related('types')

    detailed_companion_list = {}
    for companion in companions:
        base_mp_adjustment = 0
        companion_level = next((item['level'] for item in companions_list if 'slug' in item and item['slug'] == companion.slug), None)
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

    for sub_rune in sub_runes:
        if sub_rune.type:
            if sub_rune.type.name == "increase_max_mp":
                maxMp += int(sub_rune.values[0])
            elif sub_rune.type.name == "reduce_mp_for_companion_type_and_rarity":
                mp_reduction, companion_type, rarity = sub_rune.values
                for companion, data in detailed_companion_list.items():
                    if companion_type in data["types"]:
                        if rarity == "all" or rarity == data["rarity"]:
                            detailed_companion_list[companion]["mp_cost"] -= int(mp_reduction)
    total_mp_cost = sum(data["mp_cost"] for data in detailed_companion_list.values())
    return (total_mp_cost, maxMp)


def get_list_data(build_string):
    decoded_collection_string = base64.b64decode(build_string).decode('utf-8')
    _, equipment_string = decoded_collection_string.split('|')
    equipment_data = json.loads(equipment_string)
    return (
        get_equipment_info(equipment_data['companionsList'], Companion),
        get_equipment_info(equipment_data['skillList'], Skill),
        get_equipment_info(equipment_data['mainRuneList'], MainRune),
        get_equipment_info(equipment_data['subRuneList'], SubRune),
        equipment_data["mp"],
        equipment_data["baseMp"]
    )


def get_equipment_info(equipment_list, model):
    result = []
    for equipment in equipment_list:
        if 'id' in equipment:
            try:
                item = model.objects.get(id=equipment['id'])
                data = {'slug': item.slug, 'rarity': item.rarity}
                if 'level' in equipment:
                    data["level"] = equipment["level"]
                result.append(data)
            except model.DoesNotExist:
                result.append({'error': 'Item not found'})
        else:
            result.append({})
    return result
