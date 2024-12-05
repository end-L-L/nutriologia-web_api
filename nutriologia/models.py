from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Usuarios

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

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    telefono = models.CharField(max_length=15, unique=True)
    edad = models.IntegerField()
    peso = models.FloatField()
    estatura = models.FloatField()
    objetivo = models.CharField(max_length=255)
    tipo_dieta = models.IntegerField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['created']

    def __str__(self):
        return self.user.username
    
# Estadísticas

class Seguimiento_Calorico(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    calorias_recomendadas = models.PositiveIntegerField(default=0)
    calorias_consumidas = models.PositiveIntegerField(default=0)    
    calorias_excedentes = models.PositiveIntegerField(default=0)  
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Seguimiento Calorico'
        verbose_name_plural = 'Seguimiento Calorico'
        ordering = ['fecha']

    def calorias_restantes(self):
        return max(self.calorias_recomendadas - self.calorias_consumidas, 0)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"
    
class Seguimiento_Porciones(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    porciones_recomendadas = models.PositiveIntegerField(default=0)  
    porciones_consumidas = models.PositiveIntegerField(default=0)
    porciones_excedentes = models.PositiveIntegerField(default=0)  
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Seguimiento Porciones'
        verbose_name_plural = 'Seguimiento Porciones'
        ordering = ['fecha']     

    @property
    def porciones_faltantes(self):
        return max(self.porciones_recomendadas - self.porciones_consumidas, 0)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"
    
class Peso_Mensual(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    mes = models.CharField(max_length=20, null=True)        
    anio = models.PositiveIntegerField(default=0) 
    peso_inicial = models.FloatField(default=0)           
    calorias_recomendadas = models.PositiveIntegerField(default=0)  
    calorias_consumidas = models.PositiveIntegerField(default=0)    
    calorias_excedentes = models.PositiveIntegerField(default=0)  
    peso_calculado = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'Peso Mensual'
        verbose_name_plural = 'Peso Mensual'
        ordering = ['anio', 'mes']

    def calcular_peso(self):
        deficit = self.calorias_recomendadas - self.calorias_consumidas
        peso_perdido = deficit / 7700  
        return round(self.peso_inicial + self.calorias_excedentes / 7700 - peso_perdido, 2)

    def save(self, *args, **kwargs):
        if self.peso_calculado is None:
            self.peso_calculado = self.calcular_peso()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.paciente} - {self.mes} {self.anio}"