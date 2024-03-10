import json
from django.http import JsonResponse
from django.views import View
from builds.models import BuildModel
from stuff.business import calculate_mp, get_list_data, return_all_data


class GetMPInfo(View):
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            build_string = body_data.get('build_string', '')
        except (ValueError, KeyError):
            return JsonResponse({'error': 'Invalid request'}, status=400)

        return self.build_response(build_string)

    def build_response(self, build_string):
        companions_list, _, _, sub_rune_list, _, maxMp = get_list_data(build_string)
        mp, maxMp = calculate_mp(companions_list, sub_rune_list, maxMp)
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
        companions_list, skill_list, main_rune_list, sub_rune_list, mp, maxMp = get_list_data(build.build_string)
        response_data = {
            'companions': companions_list,
            'skills': skill_list,
            'mainRunes': main_rune_list,
            'subRunes': sub_rune_list,
            'mp': mp,
            'maxMp': maxMp
        }
        return JsonResponse(response_data)
