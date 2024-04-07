from django.urls import path
from .views import CreateGraphView, ExchangeCreateView

urlpatterns = [
    path("", ExchangeCreateView.as_view(), name="create"),
    path('create_graph/', CreateGraphView.as_view(), name='create_graph'),
]
