from django.contrib import admin
from django.urls import path, include 
from core.views import inicio, agregar, editar, eliminar, mostrar

urlpatterns = [
    path('', inicio, name='index'),
    path('agregar/', agregar, name='agregar'),
    path('editar/', editar, name='editar'),
    path('eliminar/', eliminar, name='eliminar'),
    path('mostar/', mostrar, name='mostrar'),
]
