from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=40, default="Nombre")
    apellido = models.CharField(max_length=20, default='Apellido')
    email = models.EmailField(max_length=40, default="email")
    nombre_usuario = models.CharField(max_length=40, default="Nombre Usuario")

    def __str__(self):
        return f"{self.nombre_usuario}"

class Post(models.Model):
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

class Mensaje(models.Model):
    emisor = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido[:50]