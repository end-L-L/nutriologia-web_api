from django.contrib import admin
from .models import Nutriologo
from .models import Paciente
from .models import Seguimiento_Calorico
from .models import Seguimiento_Porciones
from .models import Peso_Mensual

class AdminNutriologo(admin.ModelAdmin):
    list_display = ('user', 'cedula', 'telefono', 'created', 'updated')
    search_fields = ('user', 'cedula', 'telefono')
    readonly_fields = ('created', 'updated')

class AdminPaciente(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'edad', 'peso', 'estatura', 'objetivo', 'created', 'updated')
    search_fields = ('user', 'telefono', 'edad')
    readonly_fields = ('created', 'updated')

class AdminSeguimiento_Calorico(admin.ModelAdmin):
    list_display = ('paciente', 'calorias_recomendadas', 'calorias_consumidas', 'calorias_excedentes', 'fecha')
    search_fields = ('paciente', 'fecha')
    readonly_fields = ('fecha',)

class AdminSeguimiento_Porciones(admin.ModelAdmin):
    list_display = ('paciente', 'porciones_recomendadas', 'porciones_consumidas', 'porciones_excedentes', 'fecha')
    search_fields = ('paciente', 'fecha')
    readonly_fields = ('fecha')

class AdminPeso_Mensual(admin.ModelAdmin):
    list_display = ('paciente', 'mes', 'anio', 'peso_inicial','calorias_recomendadas', 'calorias_consumidas', 'calorias_excedentes')
    search_fields = ('mes', 'anio')
    

admin.site.register(Nutriologo, AdminNutriologo)
admin.site.register(Paciente, AdminPaciente)
admin.site.register(Seguimiento_Calorico, AdminSeguimiento_Calorico)
admin.site.register(Seguimiento_Porciones, AdminSeguimiento_Porciones)
admin.site.register(Peso_Mensual, AdminPeso_Mensual)