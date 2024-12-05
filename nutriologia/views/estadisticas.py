from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from nutriologia.models import *
from nutriologia.serializers import *

# Seguimiento Calorico

class SegimientoCaloricoAllView(APIView):
    def get(self, request):
        seguimientos = Seguimiento_Calorico.objects.all().order_by('-fecha')
        serializer = Seguimiento_Calorico_Serializer(seguimientos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SeguimientoCaloricoView(APIView):

    def get(self, request, id, format=None):
        try:
            paciente = get_object_or_404(Paciente, id=id)
            seguimiento = Seguimiento_Calorico.objects.filter(paciente=paciente).order_by('fecha')
            if seguimiento.exists():
                serializer = Seguimiento_Calorico_Serializer(seguimiento, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No se Encontró Registro"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Error al Obtener Registro"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = Seguimiento_Calorico_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        try:
            seguimiento = get_object_or_404(Seguimiento_Calorico, id=id)
        except Seguimiento_Calorico.DoesNotExist:
            return Response({"message": "Seguimiento Calórico no Encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Seguimiento_Calorico_Serializer(seguimiento, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Seguimiento Porciones

class SeguimientoPorcionesAllView(APIView):
    def get(self, request):
        seguimientos = Seguimiento_Porciones.objects.all().order_by('-fecha')
        serializer = Seguimiento_Porciones_Serializer(seguimientos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SeguimientoPorcionesView(APIView):
    
    def get(self, request, id, format=None):
        try:
            paciente = get_object_or_404(Paciente, id=id)
            seguimiento = Seguimiento_Porciones.objects.filter(paciente=paciente).order_by('fecha')
            if seguimiento.exists():
                serializer = Seguimiento_Porciones_Serializer(seguimiento, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No se Encontró Registro"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Error al Obtener Registro"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = Seguimiento_Porciones_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        try:
            seguimiento = get_object_or_404(Seguimiento_Porciones, id=id)
        except Seguimiento_Porciones.DoesNotExist:
            return Response({"message": "Seguimiento de Porciones no Encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Seguimiento_Porciones_Serializer(seguimiento, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Peso Mensual

class PesoMensualAllView(APIView):
    def get(self, request):
        pesos = Peso_Mensual.objects.all().order_by('-anio', 'mes')
        serializer = Peso_Mensual_Serializer(pesos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PesoMensualView(APIView):
        
    def get(self, request, id, format=None):
        try:
            paciente = get_object_or_404(Paciente, id=id)
            peso = Peso_Mensual.objects.filter(paciente=paciente).order_by('anio', 'mes')
            if peso.exists():
                serializer = Peso_Mensual_Serializer(peso, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No se Encontró Registro"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Error al Obtener Registro"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = Peso_Mensual_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        try:
            peso = get_object_or_404(Peso_Mensual, id=id)
        except Peso_Mensual.DoesNotExist:
            return Response({"message": "Peso Mensual no Encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Peso_Mensual_Serializer(peso, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)