from django.urls import path
from .views import CreateGraphView, ExchangeCreateView, GetExchangesView

urlpatterns = [
    path("", ExchangeCreateView.as_view(), name="create"),
    path('create_graph/', CreateGraphView.as_view(), name='create_graph'),
    path('get_exchanges/', GetExchangesView.as_view(), name='create_graph'),
]
