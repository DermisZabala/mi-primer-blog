from django import forms
from django.contrib.auth.forms import UserCreationForm
import re


class Usuarios(UserCreationForm):
    
    MIN_USERNAME_LENGTH = 3 # Define la longitud mínima que deseas
    
    def clean_username(self):
        '''
        clean_username() es un método especial en Django 
        que limpia y valida el campo username. 
        Al sobrescribirlo, puedes modificar su valor 
        antes de que el formulario se guarde.
        '''

        username = self.cleaned_data.get('username')

        if username: # Procede solo si se proporcionó un username

            # Convertir a minúsculas
            username_lower = username.lower()

            # Validar longitud mínima
            if len(username_lower) < self.MIN_USERNAME_LENGTH:
                raise forms.ValidationError(
                    f"El nombre de usuario debe tener al menos {self.MIN_USERNAME_LENGTH} caracteres."
                )

            # validando que el nombre tenga solo letras, numeros 0 guiones bajos
            if not re.match(r"^[a-zA-Z0-9_]+$", username_lower):
                raise forms.ValidationError(
                    "El nombre de usuario solo puede contener letras y números (sin espacios ni símbolos especiales)."
                )
            
            # Si todas las validaciones personalizadas pasan, devuelve el username en minúsculas
            return username_lower

        # Devuelve el username (o None si no se proporcionó)
        return username