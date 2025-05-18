from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Publicar(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateField(blank=True, null=True)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicar, on_delete=models.CASCADE, related_name='comentarios')

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=True) # Para moderación, si quieres ocultar comentarios

    class Meta:
        ordering = ['fecha_creacion'] # Ordena los comentarios por fecha de creación

    def __str__(self):
        return f'Comentario de {self.autor.username} en "{self.publicacion.titulo}"'