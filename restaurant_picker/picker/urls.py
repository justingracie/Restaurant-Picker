from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.all_restaurants, name='all_restaurants'),
]