from django.shortcuts import render, get_object_or_404
from .models import Publicar
from django.utils import timezone

# Create your views here.

def listas_publicaciones(request):
    publicaciones = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    return render(request, 'blog/index.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicar, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})

def sobre_mi(request):
    return render(request, 'blog/sobremi.html')

def inicio_sesion(request):
    return render(request, 'blog/inicio_sesion.html')

def registro(request):
    return render(request, 'blog/registrarse.html')

def contacto(request):
    return render(request, 'blog/contacto.html')