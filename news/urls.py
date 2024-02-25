from django.urls import path
from .views import NewsIndexView, NewsDetailView

urlpatterns = [
    path('', NewsIndexView.as_view(), name='news_index'),
    path('<slug:slug>', NewsDetailView.as_view(), name='news_detail'),
]
