from django.contrib import admin
from .models import Publicar, Comentario # importando los modelos Publicar, Comentarios

# Registrar tu modelo aqui.

admin.site.register(Publicar)
admin.site.register(Comentario)