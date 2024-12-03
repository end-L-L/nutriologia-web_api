from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Nutriologo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Nutriologo'
        verbose_name_plural = 'Nutriologos'
        ordering = ['created']

    def __str__(self):
        return self.user.username
