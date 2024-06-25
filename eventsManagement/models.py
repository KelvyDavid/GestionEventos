from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Usuarios(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name= 'customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name= 'customuser_set')

class Eventos(models.Model):
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    eventName = models.TextField()
    description = models.TextField()
    ubicacion = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering= ['timestamp']

class Inscripciones(models.Model):
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True)
