from django.urls import path
from .views import BuildCreateView, BuildDetailView

urlpatterns = [
    path("<str:build_id>/", BuildDetailView.as_view(), name="detail"),
    path("", BuildCreateView.as_view(), name="create"),
]
