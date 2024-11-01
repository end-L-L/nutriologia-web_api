from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Nutriologo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True, validators=[
        RegexValidator(regex=r'^\d{7,20}$', message="La cédula debe tener entre 7 y 20 dígitos.")
    ])
    telefono = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El teléfono debe tener entre 9 y 15 dígitos.")
    ])
    direccion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Nutriologo'
        verbose_name_plural = 'Nutriologos'
        ordering = ['created']

    def __str__(self):
        return self.user.username
