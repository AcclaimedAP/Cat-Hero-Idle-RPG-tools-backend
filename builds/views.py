from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import BuildModel


@method_decorator(csrf_exempt, name='dispatch')
class BuildCreateView(View):
    def post(self, request):
        build_string = request.body.decode('utf-8')
        if not build_string:
            return JsonResponse({'error': 'Invalid build string'}, status=400)

        build = BuildModel(build_string=build_string)
        build.save()
        return JsonResponse({'build_id': build.id}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class BuildDetailView(View):
    def get(self, request, build_id):
        try:
            build = BuildModel.objects.get(id=build_id)
            return JsonResponse({'build': build.build_string})
        except BuildModel.DoesNotExist:
            return JsonResponse({'error': 'No build found'}, status=404)
