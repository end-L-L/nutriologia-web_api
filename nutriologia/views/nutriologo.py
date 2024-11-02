
from django.contrib.auth.models  import User
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from nutriologia.models import Nutriologo
from nutriologia.serializers import UserSerializer
from nutriologia.serializers import NutriologoSerializer

class NutriologoView(APIView):

    authentication_classes = [] # no token
    #permission_classes = [AllowAny]
    
    # obtener nutriologo por ID - haciendo jwt
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        nutriologo = get_object_or_404(Nutriologo, id = request.GET.get("id"))
        nutriologo = NutriologoSerializer(nutriologo, many=False).data
        return Response(nutriologo, 200)

    # crear nutricionista
    #@authentication_classes([])
    def post(self, request, *args, **kwargs):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            password = request.data['password']
            #role = request.data['role']
            username = request.data['username']
            
            # validar email
            if User.objects.filter(email=email).exists():
                return Response({"message": "email ya registrado"}, 400)
            
            # validar username
            if User.objects.filter(username=username).exists():
                return Response({"message": "username ya registrado"}, 400)

            # crear usuario
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_active=1
            )
            
            # password encriptada
            user.set_password(password)
            user.save()

            # rol de nutriologo
            group, created = Group.objects.get_or_create(name='Nutriologo')
            group.user_set.add(user)
            user.save()

            # crear perfil de nutriologo
            nutriologo = Nutriologo.objects.create(user=user,
                                                       especialidad=request.data['especialidad'],
                                                       cedula=request.data['cedula'],
                                                       telefono=request.data['telefono'],
                                                       direccion=request.data['direccion']
                                                    )
            nutriologo.save()

            #token = get_tokens_for_user(nutriologo)
        
            return Response({"nutritionist_created_id": nutriologo.id}, 201)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # actualizar nutriologo
    permission_classes = [IsAuthenticated]
    def put(self, request, *args, **kwargs):
        nutriologo = get_object_or_404(Nutriologo, id = request.GET.get("id"))
        nutriologo.especialidad = request.data['especialidad']
        nutriologo.cedula = request.data['cedula']
        nutriologo.telefono = request.data['telefono']
        nutriologo.direccion = request.data['direccion']
        nutriologo.save()

        temp = nutriologo.user
        temp.first_name = request.data['first_name']
        temp.last_name = request.data['last_name']
        temp.save()

        user = NutriologoSerializer(nutriologo, many=False)

        return Response({"message": "nutriologo actualizado"}, 200)
    
    # eliminar nutriologo
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        nutriologo = get_object_or_404(Nutriologo, id = request.GET.get("id"))
        
        try: 
            # eliminar el usuario asoaciado
            user = nutriologo.user
            nutriologo.delete()
            user.delete()
            return Response({"message": "nutriologo eliminado"}, 200)
        except:
            return Response({"message": "error al eliminar nutriologo"}, 400)


class NutriologosAll(APIView):
    # obtener todos los nutriologos
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        nutriologos = Nutriologo.objects.all().order_by('id')
        lista = NutriologoSerializer(nutriologos, many=True)
        
        return Response(lista.data, status=status.HTTP_200_OK)