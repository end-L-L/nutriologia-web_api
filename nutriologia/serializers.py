from rest_framework import serializers
from nutriologia.models import *
from django.contrib.auth.models import User

# Usuarios

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name','last_name', 'email')

class NutriologoSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Nutriologo
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Paciente
        fields = '__all__'

# Estadísticas

class Seguimiento_Calorico_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento_Calorico
        fields = '__all__'

class Seguimiento_Porciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento_Porciones
        fields = '__all__'

class Peso_Mensual_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Peso_Mensual
        fields = '__all__'