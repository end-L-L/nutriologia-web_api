from django.urls import path, include
from rest_framework import routers
from nutriologia.views import nutriologo

router = routers.DefaultRouter()

#router.register(r'nutriologos', nutriologo.NutriologoViewSet, 'nutriologos')

urlpatterns = [
    #path("api/v1/", include(router.urls)),
    path("v1/nutriologos", nutriologo.NutriologosAll.as_view(), name="nutriologo-lista"),
    path("v1/nutriologos/crear/", nutriologo.NutriologoView.as_view(), name="nutriologo-crear"),
    path("v1/nutriologos/obtener/", nutriologo.NutriologoView.as_view(), name="nutriologo-obtener"),
    path("v1/nutriologos/actualizar/", nutriologo.NutriologoView.as_view(), name="nutriologo-actualizar"),
    path("v1/nutriologos/eliminar/", nutriologo.NutriologoView.as_view(), name="nutriologo-eliminar"),
]