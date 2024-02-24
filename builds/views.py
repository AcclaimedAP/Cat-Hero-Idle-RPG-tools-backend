from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import BuildModel
from django.utils import timezone


class BuildCreateView(View):
    def post(self, request):
        build_string = request.body.decode('utf-8').strip()
        if not build_string:
            return JsonResponse({'error': 'Invalid build string'}, status=400)

        build, created = BuildModel.objects.get_or_create(build_string=build_string)
        if created:
            build.last_accessed = timezone.now()
        status_code = 201 if created else 200  # 201 Created if new object was created, else 200 OK
        return JsonResponse({'build_id': build.id}, status=status_code)


@method_decorator(csrf_exempt, name='dispatch')
class BuildDetailView(View):
    def get(self, request, build_id):
        try:
            build = BuildModel.objects.get(id=build_id)
            return JsonResponse({'build': build.build_string})
        except BuildModel.DoesNotExist:
            return JsonResponse({'error': 'No build found'}, status=404)
