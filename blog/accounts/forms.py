from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateNewUser(UserCreationForm):
    first_name = forms.CharField(label='Nome', max_length=35)
    last_name = forms.CharField(label='Sobrenome', max_length=35)
    username = forms.CharField(label="Nome de usuário", max_length=20)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado.")
        return email
