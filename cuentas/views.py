from django.shortcuts import render, redirect
# importando las funciones para la autenticacion, logeo y cerrar sesion
from django.contrib.auth import authenticate, login, logout
# importando el formulario 'AuthenticationForm' que django proporciona para agregar nuevos usuarios
from django.contrib.auth.forms import UserCreationForm
from .forms import Usuarios
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.

def autenticar_y_login(request, username, password):
    usuario = authenticate(request, username=username, password=password)
    if usuario:
        login(request, usuario)
        return True
    return False

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        if autenticar_y_login(request, username, password):
            return redirect('listas_publicaciones')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')

    return render(request, 'blog/inicio_sesion.html')


def registro(request):
    if request.method == 'POST':
        formulario = Usuarios(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  # No guardes aún
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password1')
            usuario.save()

            grupo = Group.objects.get(name='usuarios_blog')  # asegúrate de que el grupo exista
            usuario.groups.add(grupo)
            messages.success(request, 'Cuenta creada correctamente')
            
            # Autenticar e iniciar sesión
            usuario_autenticado = authenticate(request, username=username, password=password)
            if usuario_autenticado is not None:
                login(request, usuario_autenticado)
                return redirect('listas_publicaciones')
            else:
                messages.error(request, 'Error al iniciar sesión automática')
    else:
        formulario = Usuarios()

    return render(request, 'blog/registrarse.html', {'formulario': formulario})

def cierre(request):
    logout(request)
    return redirect('listas_publicaciones')