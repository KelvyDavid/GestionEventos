from .models import Usuario, Evento
from django import forms
from django.contrib.auth.forms import UserCreationForm

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')
    first_name = forms.CharField(max_length=40, required=True, label='Nombre')
    last_name = forms.CharField(max_length=40, required=True, label='Apellido')

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese un {}'.format((self.fields[field].label)).capitalize()})
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

class EventoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre_evento', 'descripcion', 'fecha_evento', 'ubicacion', 'estado']

        widgets = {
            'fecha_evento': forms.DateInput(attrs={'type': 'date'}),
        }
