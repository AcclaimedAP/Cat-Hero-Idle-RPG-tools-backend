from django.shortcuts import render
from django.http import JsonResponse

from .models import BuildString
from django.views.decorators.csrf import csrf_exempt



def show(request, build_id):
    if build_id:
        try:
          build = BuildString.objects.get(id=build_id)
          return JsonResponse({'build': build.build_string})
        except BuildString.DoesNotExist:
          return JsonResponse({'error': 'No build found'})
    else:
        return JsonResponse({'error': 'No build id provided'})
    

@csrf_exempt
def create(request):
    if request.method == 'POST':
        build_string = request.body.decode('utf-8')
        if build_string == "":
          return JsonResponse({'error': 'Invalid build string'})
        if build_string:
            build = BuildString(build_string=build_string)
            build.save()
            print("Build ID: ", build.id)
            return JsonResponse({'build_id': build.id}, status=201)
        else:
            return JsonResponse({'error': 'No build string provided'})
    else:
        return JsonResponse({'error': 'Invalid request method'})