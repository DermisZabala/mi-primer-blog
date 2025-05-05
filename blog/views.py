from django.shortcuts import render

# Create your views here.

def listas_publicaciones(request):
    return render(request, 'blog/listas_publicaciones.html', {})