from django.urls import path
from .views import GetBuildInfo, GetMPInfo

urlpatterns = [
    path("build/<str:build_id>/", GetBuildInfo.as_view(), name="build_info"),
    path("mp/", GetMPInfo.as_view(), name="mp_info"),
]
