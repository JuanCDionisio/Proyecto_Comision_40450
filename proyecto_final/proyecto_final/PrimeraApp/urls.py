from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('posts/', views.posteos, name="Posteos"),
    path('perfiles/', views.perfiles, name="Perfiles"),
    path('mensajes/', views.mensajes, name="Mensajes"),
    path('crear-form/', views.insertar_datos, name="Crear-Form"),
    path('buscar-form/', views.buscar, name="Buscar-Form"),
]
