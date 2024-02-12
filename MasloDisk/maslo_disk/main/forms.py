from .models import Document1
from django.forms import ModelForm, TextInput, FileInput

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Document1Form(ModelForm):
    class Meta:
        model = Document1
        fields = ['title', 'file']

        widgets = {
            "title": TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Название',
            }),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
