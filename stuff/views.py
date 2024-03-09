from django.http import JsonResponse
from django.views import View
from builds.models import BuildModel
from stuff.business import calculate_mp, get_list_data


class GetMPInfo(View):
    def get(self, request):
        build_string = request.GET.get('build_string', '')
        return self.build_response(build_string)

    def build_response(self, build_string):
        companions_list, _, _, sub_rune_list = get_list_data(build_string)
        mp, maxMp = calculate_mp(companions_list, sub_rune_list)
        response_data = {
            'mp': mp,
            'maxMp': maxMp
        }
        return JsonResponse(response_data)


class GetBuildInfo(View):
    def get(self, request, build_id):
        try:
            build = BuildModel.objects.get(pk=build_id)
        except BuildModel.DoesNotExist:
            return JsonResponse({"error": "Build does not exist"})
        return self.build_response(build)

    def build_response(self, build):
        companions_list, skill_list, main_rune_list, sub_rune_list = get_list_data(build.build_string)
        mp, maxMp = calculate_mp(companions_list, sub_rune_list)
        response_data = {
            'companions': companions_list,
            'skills': skill_list,
            'mainRunes': main_rune_list,
            'subRunes': sub_rune_list,
            'mp': mp,
            'maxMp': maxMp
        }
        return JsonResponse(response_data)
