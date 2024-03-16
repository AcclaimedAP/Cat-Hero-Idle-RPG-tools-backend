import json
from django.http import JsonResponse
from django.views import View
from builds.models import BuildModel
from stuff.business import calculate_mp, get_list_data, return_all_data, get_base_mp


class GetMPInfo(View):
    def post(self, request):
        try:
            equipment_data = json.loads(request.body)
        except (ValueError, KeyError):
            return JsonResponse({'error': 'Invalid request'}, status=400)

        return self.build_response(equipment_data)

    def build_response(self, equipment_data):
        companions_list, _, _, sub_rune_list = get_list_data(equipment_data)
        baseMp = get_base_mp(equipment_data)
        mp, maxMp = calculate_mp(companions_list, sub_rune_list, baseMp)
        response_data = {
            'mp': mp,
            'maxMp': maxMp
        }
        return JsonResponse(response_data)


class GetAllStuffData(View):
    def get(self, request):
        return JsonResponse(return_all_data())


class GetBuildInfo(View):
    def get(self, request, build_id):
        try:
            build = BuildModel.objects.get(pk=build_id)
        except BuildModel.DoesNotExist:
            return JsonResponse({"error": "Build does not exist"})
        return self.build_response(build)

    def build_response(self, build):
        equipment = build.build["equipment"]
        companions_list, skill_list, main_rune_list, sub_rune_list = get_list_data(equipment)
        baseMp = get_base_mp(equipment)
        mp, maxMp = calculate_mp(companions_list, sub_rune_list, baseMp)
        response_data = {
            'companions': companions_list,
            'skills': skill_list,
            'mainRunes': main_rune_list,
            'subRunes': sub_rune_list,
            'mp': mp,
            'maxMp': maxMp
        }
        return JsonResponse(response_data)
