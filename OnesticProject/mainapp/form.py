from django import forms
from django.core import validators

# Import Python form models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # We specify the fields we want to appear in the form
        # These are fields that the user model has. They can be seen in the SQL
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']