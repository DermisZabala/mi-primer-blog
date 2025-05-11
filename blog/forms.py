# creacion del formulario 
from django import forms
from .models import Publicar

class PublicarForm(forms.ModelForm):
    class Meta:
        model = Publicar
        fields = ('titulo', 'texto',)