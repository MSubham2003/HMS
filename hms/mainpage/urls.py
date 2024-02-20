from django.contrib import admin
from django.urls import path
from mainpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('developers/', views.teamprofile, name='developers')
]
