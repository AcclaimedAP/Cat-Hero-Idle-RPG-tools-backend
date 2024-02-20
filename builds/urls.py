from django.urls import path

from . import views

urlpatterns = [
    path("<int:build_id>/", views.show, name="show"),
    path("new/", views.create, name="create"),
]