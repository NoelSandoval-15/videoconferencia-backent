from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.entrevistas.models import Entrevista
from apps.usuarios.models import Usuario

from .models import Sesion
from .serializers import CrearSesionSerializer, SesionSerializer


class CrearObtenerSesionView(APIView):
    def post(self, request):
        serializer = CrearSesionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        entrevista_id = serializer.validated_data["entrevista_id"]
        creada_por_id = serializer.validated_data["creada_por"]

        try:
            entrevista = Entrevista.objects.get(pk=entrevista_id)
        except Entrevista.DoesNotExist:
            return Response({"detail": "Entrevista no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        try:
            usuario = Usuario.objects.get(pk=creada_por_id)
        except Usuario.DoesNotExist:
            return Response({"detail": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        sesion_activa = Sesion.objects.filter(
            entrevista=entrevista, estado=Sesion.Estado.ACTIVA
        ).first()

        if sesion_activa:
            return Response(SesionSerializer(sesion_activa).data, status=status.HTTP_200_OK)

        sesion = Sesion.objects.create(entrevista=entrevista, creada_por=usuario)
        return Response(SesionSerializer(sesion).data, status=status.HTTP_201_CREATED)

    def get(self, request, entrevista_id):
        try:
            entrevista = Entrevista.objects.get(pk=entrevista_id)
        except Entrevista.DoesNotExist:
            return Response({"detail": "Entrevista no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        sesion = Sesion.objects.filter(
            entrevista=entrevista, estado=Sesion.Estado.ACTIVA
        ).first()

        if not sesion:
            return Response({"detail": "No hay sesión activa para esta entrevista."}, status=status.HTTP_404_NOT_FOUND)

        return Response(SesionSerializer(sesion).data, status=status.HTTP_200_OK)


class FinalizarSesionView(APIView):
    def patch(self, request, sesion_id):
        try:
            sesion = Sesion.objects.get(pk=sesion_id)
        except Sesion.DoesNotExist:
            return Response({"detail": "Sesión no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        from django.utils import timezone
        sesion.estado = Sesion.Estado.FINALIZADA
        sesion.fecha_fin = timezone.now()
        sesion.save()

        return Response(SesionSerializer(sesion).data, status=status.HTTP_200_OK)
