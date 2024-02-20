from django.contrib import admin
from django.urls import path
from userstudent import views

urlpatterns = [
    path('', views.studentlogin, name='studentlogin'),
    path('register/', views.studentregister, name='studentregister')
]
