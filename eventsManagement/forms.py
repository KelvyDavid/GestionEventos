from .models import Usuarios
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class DatosUserCreacionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuarios
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuarios.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuarios.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username