from django import forms
from django.db import models
from django.forms.widgets import PasswordInput, Select, TextInput
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'name': 'search_box',
        'placeholder': "Create Your Task"
    }))

    class Meta:
        model = Todo
        fields = ["title", 'status']


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'type': 'text',
        'placeholder': "Enter Your Username",
        'name': 'username'
    }))
    email = forms.EmailField(widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'type': 'email',
        'placeholder': "Enter Your Email Address",
        'name': 'email',
    }))
    password1 = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'password1',
        'type': 'password',
        'placeholder': "Enter Your Password",
        'name': 'password1',
    }))
    password2 = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'password2',
        'type': 'password',
        'placeholder': "Confirm Your Password",
        'name': 'password2',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
