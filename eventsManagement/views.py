from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from eventsManagement.forms import DatosUserCreacionForm
from eventsManagement.models import Usuarios

# Create your views here.
class RegistroView(CreateView):
    form_class = DatosUserCreacionForm
    template_name = 'registro.html'
    success_url = reverse_lazy('gestionEventos')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            login(self.request, self.object)
            return response
        except Exception as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        for error in form.error.values():
            messages.error(self.request, error)
            return super().form_invalid(form)
        

class LoginView(CreateView):
    form_class = DatosUserCreacionForm
    template_name = 'login.html'
    success_url = reverse_lazy('gestionEventos')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            login(self.request, self.object)
            return response
        except Exception as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        for error in form.error.values():
            messages.error(self.request, error)
            return super().form_invalid(form)