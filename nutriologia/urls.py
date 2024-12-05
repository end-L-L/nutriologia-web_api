from django.urls import path, include
from rest_framework import routers
from nutriologia.views import nutriologo
from nutriologia.views import paciente
from nutriologia.views import estadisticas

router = routers.DefaultRouter()

#router.register(r'nutriologos', nutriologo.NutriologoViewSet, 'nutriologos')

urlpatterns = [
    #path("api/v1/", include(router.urls)),
    
    # nutriologos 

    path("v1/nutriologos/", nutriologo.NutriologosAll.as_view(), name="nutriologo-lista"),
    path("v1/nutriologos/crear/", nutriologo.NutriologoViewPublic.as_view(), name="nutriologo-crear"),
    path("v1/nutriologos/obtener/", nutriologo.NutriologoView.as_view(), name="nutriologo-obtener"),
    path("v1/nutriologos/actualizar/", nutriologo.NutriologoView.as_view(), name="nutriologo-actualizar"),
    path("v1/nutriologos/eliminar/", nutriologo.NutriologoView.as_view(), name="nutriologo-eliminar"),

    # pacientes
    
    path("v1/pacientes/", paciente.PacientesAll.as_view(), name="paciente-lista"),
    path("v1/pacientes/crear/", paciente.PacienteViewPublic.as_view(), name="paciente-crear"),
    path("v1/pacientes/obtener/<int:id>", paciente.PacienteView.as_view(), name="paciente-obtener"),
    path("v1/pacientes/actualizar/<int:id>", paciente.PacienteView.as_view(), name="paciente-actualizar"),
    path("v1/pacientes/eliminar/<int:id>", paciente.PacienteView.as_view(), name="paciente-eliminar"),

    # seguimiento calorico
    
    path("v1/paciente/s-caloricos/", estadisticas.SegimientoCaloricoAllView.as_view(), name="s-caloricos"),
    path("v1/paciente/s-calorico/crear/", estadisticas.SeguimientoCaloricoView.as_view(), name="s-calorico-crear"),
    path("v1/paciente/s-calorico/obtener/<int:id>", estadisticas.SeguimientoCaloricoView.as_view(), name="s-calorico-obtener"),
    path("v1/paciente/s-calorico/actualizar/<int:id>", estadisticas.SeguimientoCaloricoView.as_view(), name="s-calorico-actualizar"),

    # seguimiento porciones
    
    path("v1/paciente/s-porciones/", estadisticas.SeguimientoPorcionesAllView.as_view(), name="s-porciones"),
    path("v1/paciente/s-porciones/crear/", estadisticas.SeguimientoPorcionesView.as_view(), name="s-porciones-crear"),
    path("v1/paciente/s-porciones/obtener/<int:id>", estadisticas.SeguimientoPorcionesView.as_view(), name="s-porciones-obtener"),
    path("v1/paciente/s-porciones/actualizar/<int:id>", estadisticas.SeguimientoPorcionesView.as_view(), name="s-porciones-actualizar"),

    # peso mensual

    path("v1/paciente/pesos/", estadisticas.PesoMensualAllView.as_view(), name="pesos"),
    path("v1/paciente/peso/crear/", estadisticas.PesoMensualView.as_view(), name="peso-crear"),
    path("v1/paciente/peso/obtener/<int:id>", estadisticas.PesoMensualView.as_view(), name="peso-obtener"),
    path("v1/paciente/peso/actualizar/<int:id>", estadisticas.PesoMensualView.as_view(), name="peso-actualizar")
]