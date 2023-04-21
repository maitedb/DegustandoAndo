from django.contrib import admin
from django.urls import path, include
from core.views import inicio, editar, eliminar
from user.views import * 

urlpatterns = [
    path('', inicio, name='index'),
    path('agregar/', agregarpostlogueo, name='agregar'),
    path('editar//<int:id_articulo>/', editar, name='editar'),
    path('eliminar/<int:id_articulo>/',eliminar, name='eliminar'),
    path('mostrar/', mostrarpostlogueo, name='mostrar'),
    path('logout/', exit, name='exit'),
    path('register/', register, name= 'register')
]
