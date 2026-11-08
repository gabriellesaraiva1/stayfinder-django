from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, label="Nome")
    email = forms.EmailField(label="E-mail")
    class Meta:
        model = User
        fields = ("first_name", "username", "email", "password1", "password2")
        labels = {"username": "Usuário", "password1": "Senha", "password2": "Confirme a senha"}
