from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    photo=forms.ImageField()
    class Meta:
        model=User
        fields=["username","email","first_name","last_name","password1","password2","photo"]
