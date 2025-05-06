from django.shortcuts import render
from .models import Publicar
from django.utils import timezone

# Create your views here.

def listas_publicaciones(request):
    publicaciones = Publicar.objects.filter().order_by('fecha_publicacion')
    return render(request, 'blog/listas_publicaciones.html', {'publicaciones': publicaciones})
