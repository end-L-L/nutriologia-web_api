from django.contrib.auth.models  import User
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.db import transaction

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from nutriologia.models import Paciente
from nutriologia.serializers import UserSerializer
from nutriologia.serializers import PacienteSerializer

# public view sin autenticación
class PacienteViewPublic(APIView):
    
    # no auth
    authentication_classes = [] # no token
    permission_classes = [AllowAny]
    
    # crear paciente
    def post(self, request, *args, **kwargs):
    
        user = UserSerializer(data=request.data)
        
        try:
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

                # validar telefono
                telefono = request.data['telefono']
                if len(telefono) < 8 or len(telefono) > 15:
                    return Response({"message": "El teléfono debe tener entre 8 y 15 dígitos."}, 400)

                telefono_paciente = Paciente.objects.filter(telefono=request.data['telefono'])
                if telefono_paciente.exists():
                    return Response({"message": "Teléfono ya registrado"}, 400)
                
                # crear usuario
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    is_active=1
                )

                # rol de paciente
                group, created = Group.objects.get_or_create(name='paciente')
                group.user_set.add(user)

                # crear perfil de paciente
                paciente = Paciente.objects.create(user=user,
                                                        telefono=request.data['telefono'],
                                                        edad=request.data['edad'],
                                                        peso=request.data['peso'],
                                                        estatura=request.data['estatura'],
                                                        objetivo=request.data['objetivo'],
                                                        tipo_dieta=request.data['tipo_dieta']
                                                        )
                
                paciente.save()

                return Response({"patient_created_id": paciente.id}, 201)
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "error al crear paciente"}, 400)
        

class PacientesAll(APIView):
    # no auth
    authentication_classes = [] # no token
    permission_classes = [AllowAny]

    # obtener todos los pacientes
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.all().order_by('id')
        lista = PacienteSerializer(pacientes, many=True)
        
        return Response(lista.data, status=status.HTTP_200_OK)
    
class PacienteView(APIView):
    
    # paciente id
    def get(self, request, id, format=None):
        try:
            # obtener el paciente por ID desde la URL
            paciente = get_object_or_404(Paciente, id=id)
            user = paciente.user

            # serializar los datos del paciente
            paciente_data = PacienteSerializer(paciente).data

            grupo_paciente = user.groups.filter(name="paciente").first()
            paciente_data['rol'] = grupo_paciente.name if grupo_paciente else "s/r"

            return Response(paciente_data, status=status.HTTP_200_OK)
        
        except Paciente.DoesNotExist:
            return Response({"message": "Paciente no Encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Error al Obtener Paciente."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # actualizar paciente
    def put(self, request, id, format=None):
        try:
            paciente = get_object_or_404(Paciente, id=id)
            print(paciente.id)
        except Paciente.DoesNotExist:
            return Response({"message": "Paciente no Encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        # actualizar datos del paciente
        paciente_serializer = PacienteSerializer(paciente, data=request.data, partial=True)
        
        if paciente_serializer.is_valid():
            paciente_serializer.save()
            return Response(paciente_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(paciente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    # eliminar paciente
    def delete(self, request, id, format=None):
        
        paciente = get_object_or_404(Paciente, id=id)
        user = paciente.user

        # transacción atómica
        with transaction.atomic():
            try:
                # eliminar paciente y usuario asociado
                paciente.delete()
                user.delete()
                return Response({"mensaje": "Cuenta Eliminada Exitosamente."}, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response(
                    {"mensaje": "Error al Eliminar la Cuenta.", "detalle": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )