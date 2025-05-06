from django.shortcuts import render
from .models import Publicar
from django.utils import timezone

# Create your views here.

def listas_publicaciones(request):
    publicaciones = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'blog/index.html', {'publicaciones': publicaciones})
