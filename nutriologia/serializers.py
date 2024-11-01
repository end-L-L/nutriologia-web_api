from rest_framework import serializers
from nutriologia.models import Nutriologo
from django.contrib.auth.models import User

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