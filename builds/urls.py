from django.urls import path
from .views import BuildView

urlpatterns = [
    path("<str:build_id>/", BuildView.as_view(), name="show"),
    path("new/", BuildView.as_view(), name="create"),
]
