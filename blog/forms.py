# creacion del formulario 
from django import forms
from .models import Publicar, Comentario

class PublicarForm(forms.ModelForm):
    class Meta:
        model = Publicar
        fields = ('titulo', 'texto',)

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',) # Solo necesitamos el campo de texto del usuario
        widgets = {
            'texto': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escribe tu comentario aquí...'
            }),
        }
        labels = {
            'texto': '', # No mostrar la etiqueta "Texto:" explícitamente
        }