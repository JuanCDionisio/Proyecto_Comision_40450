from django.shortcuts import render, redirect
from .models import Perfil, Post, Mensaje
from .forms import PerfilForm, PostForm, MensajeForm, BuscarForm

def inicio(request):
    return render(request, "PrimeraApp/index.html")

def about(request):
    return render(request, "PrimeraApp/about.html")

def posteos(request):
    return render(request, "PrimeraApp/posts.html")

def perfiles(request):
    return render(request, "PrimeraApp/perfiles.html")

def mensajes(request):
    return render(request, "PrimeraApp/mensajes.html")

def insertar_datos(request):
    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST, prefix='perfil')
        post_form = PostForm(request.POST, prefix='post')
        mensaje_form = MensajeForm(request.POST, prefix='mensaje')

        if 'perfil_submit' in request.POST:
            # Guardar formulario de Perfil
            if perfil_form.is_valid():
                perfil = perfil_form.save()
                return redirect('Inicio')  # Reemplaza 'nombre_de_la_vista' con la vista a la que deseas redirigir

        elif 'post_submit' in request.POST:
            # Guardar formulario de Post
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.autor = Perfil.objects.first()  # Reemplaza esto con la lógica para obtener el perfil adecuado
                post.save()
                return redirect('Inicio')  # Reemplaza 'nombre_de_la_vista' con la vista a la que deseas redirigir

        elif 'mensaje_submit' in request.POST:
            # Guardar formulario de Mensaje
            if mensaje_form.is_valid():
                mensaje = mensaje_form.save()
                return redirect('Inicio')  # Reemplaza 'nombre_de_la_vista' con la vista a la que deseas redirigir

    else:
        perfil_form = PerfilForm(prefix='perfil')
        post_form = PostForm(prefix='post')
        mensaje_form = MensajeForm(prefix='mensaje')

    return render(request, 'PrimeraApp/crear_form.html', {
        'perfil_form': perfil_form,
        'post_form': post_form,
        'mensaje_form': mensaje_form,
    })

def buscar(request):
    if request.method == 'POST':
        buscar_form = BuscarForm(request.POST)
        if buscar_form.is_valid():
            busqueda = buscar_form.cleaned_data['busqueda']
            # Realiza la lógica de búsqueda en la base de datos
            perfiles = Perfil.objects.filter(nombre__icontains=busqueda) | \
                       Perfil.objects.filter(apellido__icontains=busqueda) | \
                       Perfil.objects.filter(email__icontains=busqueda) | \
                       Perfil.objects.filter(nombre_usuario__icontains=busqueda)
            
            posts = Post.objects.filter(titulo__icontains=busqueda) | \
                    Post.objects.filter(contenido__icontains=busqueda)
            
            mensajes = Mensaje.objects.filter(contenido__icontains=busqueda)
            
            return render(request, 'PrimeraApp/resultado_busqueda.html', {
                'buscar_form': buscar_form,
                'perfiles': perfiles,
                'posts': posts,
                'mensajes': mensajes
            })
    else:
        buscar_form = BuscarForm()
    return render(request, 'PrimeraApp/buscar_form.html', {
    'buscar_form': buscar_form
})

