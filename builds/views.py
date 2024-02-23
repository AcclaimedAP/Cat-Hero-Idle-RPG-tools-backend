from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import BuildModel


@method_decorator(csrf_exempt, name='dispatch')
class BuildView(View):
    def get(self, request, build_id):
        if build_id:
            try:
                build = BuildModel.objects.get(id=build_id)
                return JsonResponse({'build': build.build_string})
            except BuildModel.DoesNotExist:
                return JsonResponse({'error': 'No build found'})
        else:
            return JsonResponse({'error': 'No build id provided'})

    def post(self, request):
        build_string = request.body.decode('utf-8')
        if build_string == "":
            return JsonResponse({'error': 'Invalid build string'})
        if build_string:
            build = BuildModel(build_string=build_string)
            build.save()
            print("Build ID: ", build.id)
            return JsonResponse({'build_id': build.id}, status=201)
        else:
            return JsonResponse({'error': 'No build string provided'})
