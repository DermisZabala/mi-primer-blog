from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicar
from django.utils import timezone
from .forms import PublicarForm
from django.contrib.auth.decorators import login_required 

# Create your views here.

def listas_publicaciones(request):
    publicaciones = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_creacion')
    
    return render(request, 'blog/index.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicar, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})

def sobre_mi(request):
    return render(request, 'blog/sobremi.html')

# def inicio_sesion(request):
#     return render(request, 'blog/inicio_sesion.html')

# def registro(request):
#     return render(request, 'blog/registrarse.html')

def contacto(request):
    return render(request, 'blog/contacto.html')



@login_required
def nueva_publicacion(request):
    titulo = "Crear Publicaciones"
    if request.method == "POST":
        formulario = PublicarForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_publicacion = timezone.now()
            publicacion.publicacion()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        formulario = PublicarForm()
   
    return render(request, 'blog/nueva_publicacion.html', {'formulario': formulario, 'titulo': titulo})

def editar_publicacion(request, pk):
    titulo = "Editar Publicaciones"
    publicacion = get_object_or_404(Publicar, pk=pk)
    if request.method == "POST":
        formulario = PublicarForm(request.POST, instance=publicacion)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_publicacion = timezone.now()
            publicacion.publicacion()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        formulario = PublicarForm(instance=publicacion)
    
    context = {
        'formulario': formulario,
        'titulo': titulo,
        'publicacion': publicacion
    }
   
    return render(request, 'blog/editar_publicacion.html', context)
 