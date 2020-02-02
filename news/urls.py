
from django.urls import path
from . import views


urlpatterns = [
    path('<int:category_id>/', views.by_category, name='by_category'),
    path('', views.index, name='index'),
    path('api/', views.api_news),
]