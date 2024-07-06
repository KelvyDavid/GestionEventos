from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('normal', 'Usuario Normal'),
    )

    rol = models.CharField(max_length=7, choices=ROLES, default='normal')

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_evento = models.DateField()
    ubicacion = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
    inscritos = models.ManyToManyField(Usuario, related_name='eventos_inscritos', through= 'Inscripcion', blank=True)

    def __str__(self):
        return self.nombre_evento
    
class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'evento')
