from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from eventsManagement.forms import RegistroUsuarioForm, EventoForm
from eventsManagement.models import Evento

# Create your views here.

# Esta vista son para el login de la aplicacion
class CustomLoginView(LoginView):
    template_name = 'registro/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos. Por favor, ingrese nuevamente.')
        return super().form_invalid(form)

# Esta vista es para cerrar la sesión
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Sesión cerrada correctamente.')
        response = redirect('login')
        response['Cache-Control']= 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    
# Esta vista es para registrar un usuario
class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registro/registro.html'
    success_url = reverse_lazy('tabla_eventos')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, "Se ha registrado exitosamente.")
        return response
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)

# Esta vista es para ver la lista de eventos
class ListaEventosView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'eventos/tabla_eventos.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        if self.request.user.rol == 'admin':
            return Evento.objects.all()
        return Evento.objects.filter(estado=True)

# Esta vista es para crear un evento
class CrearEventoView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/formulario_eventos.html'
    success_url = reverse_lazy('tabla_eventos')

    def test_func(self):
        return self.request.user.rol == 'admin'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El evento se ha creado correctamente')
        return response

# Esta vista es para ver la lista de eventos en las que se esta inscrito.
class MisEventosView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'eventos/tabla_eventos.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        return self.request.user.eventos_inscritos.all()

# Esta vista es para ver el detalle del evento.
class DetalleEventoView(LoginRequiredMixin, DetailView):
    model = Evento
    template_name = 'eventos/detalle_eventos.html'
    context_object_name = 'evento'

# Esta vista es para inscribirse a un evento
class InscribirEventoView(LoginRequiredMixin, DetailView):
    model = Evento

    def get(self, request, *args, **kwargs):
        evento = self.get_object()
        if request.user not in evento.inscritos.all() and evento.inscritos.count() < evento.cupos:
            evento.inscritos.add(request.user)
            messages.success(request, f'Se ha inscrito exitosamente en el evento {evento.nombre_evento}')
        else:
            messages.error(request, 'No se pudo realizar la inscripción. El evento puede estar lleno o ya está inscrito ')
        return redirect('detalle_eventos', pk=evento.pk)
