# from django.contrib import admin
from django.urls import path

from billetterie import views

urlpatterns = [
    path('', views.index, name='index'),
    path('réservations/', views.booking, name='réservations'),
]
