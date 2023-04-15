from django.contrib import admin
from django.urls import path, include 
from core.views import inicio, agregar, editar, eliminar, mostrar

urlpatterns = [
    path('', inicio, name='index'),
    path('agregar/', agregar, name='agregar'),
    path('editar//<int:id_articulo>/', editar, name='editar'),
    path('eliminar/<int:id_articulo>/',eliminar, name='eliminar'),
    path('mostrar/', mostrar, name='mostrar'),
]
