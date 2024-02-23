from django.urls import path

from . import views

urlpatterns = [
    path("list/<str:build_id>/", views.show, name="show"),
    path("new/", views.create, name="create"),
]