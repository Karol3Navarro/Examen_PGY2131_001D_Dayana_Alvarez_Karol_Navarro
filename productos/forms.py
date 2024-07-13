from django import forms
from .models import Categoria 

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #Nuevo
from django.contrib.auth.models import User #Nuevo

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria",]
        labels ={'categoria': 'Categoría',}

class CustomUserCreationForm(UserCreationForm):
    pass
    #class Meta:
     #   model = User
      #  fields = ['username', "first_name", "last_name", "email", 'password1', 'password2']