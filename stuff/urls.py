from django.urls import path
from .views import GetBuildInfo

urlpatterns = [
    path("<str:build_id>/", GetBuildInfo.as_view(), name="build_info"),
]
