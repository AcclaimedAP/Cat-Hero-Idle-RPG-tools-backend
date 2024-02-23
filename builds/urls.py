from django.urls import path

from . import views

urlpatterns = [
    path("new/", views.create, name="create"),
    path("/<str:build_id>/", views.show, name="show"),
]