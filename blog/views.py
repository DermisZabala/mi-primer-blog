from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicar, Comentario
from django.utils import timezone
from .forms import PublicarForm, FormularioComentario
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def listas_publicaciones(request):
    publicaciones = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_creacion')
    
    return render(request, 'blog/index.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicar, pk=pk)

    # Obtener comentarios activos para esta publicación
    comentarios = publicacion.comentarios.filter(activo=True)
    nuevo_comentario = None # Inicializar

    if request.method == 'POST':
        # Un comentario fue enviado
        form_comentario = FormularioComentario(data=request.POST)
        if form_comentario.is_valid():
            # Crear el objeto Comentario pero no guardarlo en la BD todavía
            nuevo_comentario = form_comentario.save(commit=False)
            # Asignar la publicación actual al comentario
            nuevo_comentario.publicacion = publicacion
            # Asignar el usuario actual como autor del comentario
            if request.user.is_authenticated: # Asegurarse que el usuario está logueado
                nuevo_comentario.autor = request.user
                nuevo_comentario.save()
                messages.success(request, '¡Tu comentario ha sido añadido!')
                # Redirigir a la misma página para ver el comentario y limpiar el form
                return redirect('detalle_publicacion', pk=publicacion.pk)
            else:
                # Esto no debería pasar si decoras la vista o el envío del form
                messages.error(request, 'Debes iniciar sesión para comentar.')
        else:
            messages.error(request, 'Hubo un error con tu comentario. Por favor, inténtalo de nuevo.')
    else: # Método GET
        form_comentario = FormularioComentario()

    context = {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
    }

    return render(request, 'blog/detalle_publicacion.html', context)

@login_required # Solo usuarios logueados pueden intentar eliminar
def eliminar_comentario_view(request, pk_comentario):
    # Obtener el comentario o devolver un 404 si no existe
    comentario_a_eliminar = get_object_or_404(Comentario, pk=pk_comentario)
    
    # Guardar el ID de la publicación para la redirección ANTES de eliminar el comentario
    id_publicacion_original = comentario_a_eliminar.publicacion.pk

    # Lógica de permisos:
    # Opción 1: Solo el autor del comentario puede eliminarlo.
    # if request.user == comentario_a_eliminar.autor:
    #
    # Opción 2: El autor del comentario O el autor de la publicación pueden eliminarlo.
    # if request.user == comentario_a_eliminar.autor or request.user == comentario_a_eliminar.publicacion.autor:
    #
    # Opción 3: El autor del comentario, el autor de la publicación O un superusuario/staff pueden eliminarlo.
    if request.user == comentario_a_eliminar.autor or \
       request.user == comentario_a_eliminar.publicacion.autor or \
       request.user.is_staff: # o request.user.is_superuser

        if request.method == 'POST': # Asegurarse que la eliminación se hace por POST
            comentario_a_eliminar.delete()
            messages.success(request, 'Comentario eliminado correctamente.')
        else:
            # Si se accede por GET, no hacer nada o mostrar un error/confirmación
            # Por simplicidad, aquí no haremos nada con GET y solo permitiremos POST.
            # Podrías redirigir o mostrar una página de confirmación si quisieras.
            messages.warning(request, 'La eliminación de comentarios debe hacerse mediante POST.')
            
    else:
        # El usuario no tiene permiso
        messages.error(request, 'No tienes permiso para eliminar este comentario.')

    # Redirigir de vuelta a la página de detalle de la publicación original
    return redirect('detalle_publicacion', pk=id_publicacion_original)



def sobre_mi(request):
    return render(request, 'blog/sobremi.html')

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

