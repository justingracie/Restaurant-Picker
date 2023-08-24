from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.restaurant_list, name='restaurant-list'),
    path('choose-for-me/', views.choose_for_me, name='choose-for-me'),
]