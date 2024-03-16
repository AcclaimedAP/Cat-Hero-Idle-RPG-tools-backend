from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import BuildModel
from django.utils import timezone
import json


@method_decorator(csrf_exempt, name='dispatch')
class BuildCreateView(View):
    def post(self, request):
        try:
            build_data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        if not build_data:
            return JsonResponse({'error': 'Empty Build'}, status=400)

        build, created = BuildModel.objects.get_or_create(build=build_data)
        if created:
            build.last_accessed = timezone.now()
            build.save(update_fields=['last_accessed'])

        status_code = 201 if created else 200
        return JsonResponse({'build_id': build.id}, status=status_code)


@method_decorator(csrf_exempt, name='dispatch')
class BuildDetailView(View):
    def get(self, request, build_id):
        try:
            build = BuildModel.objects.get(id=build_id)
            return JsonResponse({'build': build.build})
        except BuildModel.DoesNotExist:
            return JsonResponse({'error': 'No build found'}, status=404)
