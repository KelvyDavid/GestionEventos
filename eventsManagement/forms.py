from .models import Usuarios
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class DatosUserCreacionForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = Usuarios
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

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
    
class InicioSesionForm(AuthenticationForm):
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