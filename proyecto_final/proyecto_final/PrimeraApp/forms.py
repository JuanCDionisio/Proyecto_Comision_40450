from django import forms
from .models import Perfil, Post, Mensaje

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'email', 'nombre_usuario']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['autor', 'titulo', 'contenido']

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['emisor', 'receptor', 'contenido']

class BuscarForm(forms.Form):
    busqueda = forms.CharField()


