from django.urls import path
from .views import (
    GetAllStuffData, GetBuildInfo, GetMPInfo,
    export_companions_csv, export_skills_csv, export_types_csv,
    export_runetypes_csv, export_subrunes_csv, export_mainrunes_csv,
    export_all_csv
)

urlpatterns = [
    path("", GetAllStuffData.as_view(), name="get_all_stuff_data"),
    path("build/<str:build_id>/", GetBuildInfo.as_view(), name="build_info"),
    path("mp/", GetMPInfo.as_view(), name="mp_info"),
    path("export/companions/", export_companions_csv, name="export_companions_csv"),
    path("export/skills/", export_skills_csv, name="export_skills_csv"),
    path("export/types/", export_types_csv, name="export_types_csv"),
    path("export/runetypes/", export_runetypes_csv, name="export_runetypes_csv"),
    path("export/subrunes/", export_subrunes_csv, name="export_subrunes_csv"),
    path("export/mainrunes/", export_mainrunes_csv, name="export_mainrunes_csv"),
    path("export/all/", export_all_csv, name="export_all_csv"),
]
