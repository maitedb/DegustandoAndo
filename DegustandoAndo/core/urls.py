from django.contrib import admin
from django.urls import path, include 
from core.views import inicio

urlpatterns = [
    path('', inicio, name='index')
]
