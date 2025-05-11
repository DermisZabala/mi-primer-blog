from django.shortcuts import render, redirect
# importando las funciones para la autenticacion, logeo y cerrar sesion
from django.contrib.auth import authenticate, login, logout
# importando el formulario 'AuthenticationForm' que django proporciona para agregar nuevos usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('listas_publicaciones')
    else:
        messages.error(request, 'Usuario o contraseña incorrecto')

    return render(request, 'blog/inicio_sesion.html')

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.save()
            grupo = Group.objects.get(name='usuarios_blog')  # asegúrate de que el grupo exista
            usuario.groups.add(grupo)
            messages.success(request, 'Cuenta creada correctamente')
            return redirect('listas_publicaciones')
    else:
        formulario = UserCreationForm()

    return render(request, 'blog/registrarse.html', {'formulario': formulario})

def cierre(request):
    logout(request)
    return redirect('listas_publicaciones')