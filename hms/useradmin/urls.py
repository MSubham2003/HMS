from django.contrib import admin
from django.urls import path
from useradmin import views

urlpatterns = [
    path('', views.adminlogin, name='adminlogin')
]
