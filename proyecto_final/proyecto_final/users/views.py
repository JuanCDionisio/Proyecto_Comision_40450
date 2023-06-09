from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserEditForm, AvatarForm, MyUserEditForm
from .forms import UserRegisterForm
from .models import Avatar
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy
from .forms import CambiarPasswordForm

# Create your views here.
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "PrimeraApp/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "PrimeraApp/index.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "PrimeraApp/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})

# Vista de registro
def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"PrimeraApp/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:      
        form = UserRegisterForm()     

    return render(request,"users/registro.html" ,  {"form":form})

# Vista de editar el perfil
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = MyUserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            # Obtener o crear el objeto Avatar asociado al usuario
            avat, created = Avatar.objects.get_or_create(user=usuario)

            if 'avatar' in request.FILES:
                avat.imagen = request.FILES['avatar']
                avat.save()

            return render(request, "PrimeraApp/index.html")
    else:
        miFormulario = MyUserEditForm(
            initial={
                'email': usuario.email,
                'last_name': usuario.last_name,
                'first_name': usuario.first_name
            }
        )

    return render(
        request,
        "users/editarPerfil.html",
        {
            "miFormulario": miFormulario,
            "usuario": usuario
        }
    )


class CambiarPasswordView(LoginRequiredMixin, View):
    template_name = "users/cambiar_pass.html"
    form_class = CambiarPasswordForm
    success_url = reverse_lazy("Inicio")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})
    
    def post(self, request, *args, **kwargs):
        
        usuario = User.objects.get(id=request.user.id)
        form = self.form_class(request.POST)
        
        if form.is_valid():
            pass1 = form.cleaned_data.get("password1")
            pass2 = form.cleaned_data.get("password2")
        
            if pass1 == pass2:
                usuario.set_password(pass1)
                usuario.save()
                return render(request, "PrimeraApp/index.html")