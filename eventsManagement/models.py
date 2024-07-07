from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# El modelo Usuario hereda los atributos de la clase AbstractUser y agrega los roles de administrador y usuario normal
# Cuando se crea un nuevo usuario en la pagina web, por defecto sera un usuario normal
class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('normal', 'Usuario Normal'),
    )

    rol = models.CharField(max_length=7, choices=ROLES, default='normal')

# El modelo Evento hereda los atributos de la clase models.Model y agrega los campos nombre_evento, descripcion, fecha_evento, ubicacion, cupos, estado y inscritos
class Evento(models.Model):
    nombre_evento = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_evento = models.DateField()
    ubicacion = models.CharField(max_length=150)
    cupos = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)
    inscritos = models.ManyToManyField(Usuario, related_name='eventos_inscritos', through= 'Inscripcion', blank=True)

    def __str__(self):
        return self.nombre_evento

#   El modelo Inscripcion hereda los atributos de la clase models.Model y agrega los campos usuario, evento y fecha_inscripcion
class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'evento')
