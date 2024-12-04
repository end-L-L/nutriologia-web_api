from django.urls import path, include
from rest_framework import routers
from nutriologia.views import nutriologo
from nutriologia.views import paciente

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
]