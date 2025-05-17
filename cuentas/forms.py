from django import forms
from django.contrib.auth.forms import UserCreationForm


class Usuarios(UserCreationForm):
    def clean_username(self):
        '''
        clean_username() es un método especial en Django 
        que limpia y valida el campo username. 
        Al sobrescribirlo, puedes modificar su valor 
        antes de que el formulario se guarde.
        '''
        username = self.cleaned_data.get('username')

        if username:
            # Convierte a minúsculas
            return username.lower()
        
        return username
    

