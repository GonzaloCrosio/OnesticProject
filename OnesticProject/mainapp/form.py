from django import forms
from django.core import validators

# Importo los modelos de formularios de Python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # Ahora indicamos los campos que queremos que se vean en el formulario.
        # Y son campos que tiene el modelo de usuario. Se pueden ver en el SQL
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']