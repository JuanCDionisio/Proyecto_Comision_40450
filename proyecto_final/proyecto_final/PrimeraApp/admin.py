from django.contrib import admin
from .models import Perfil, Mensaje, Post
# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'nombre_usuario']

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ['emisor', 'receptor', 'contenido', 'fecha_envio']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['autor', 'titulo', 'contenido', 'fecha_publicacion']
