from django.urls import path
from .views import GetAllStuffData, GetBuildInfo, GetMPInfo

urlpatterns = [
    path("", GetAllStuffData.as_view(), name="get_all_stuff_data"),
    path("build/<str:build_id>/", GetBuildInfo.as_view(), name="build_info"),
    path("mp/", GetMPInfo.as_view(), name="mp_info"),
]
