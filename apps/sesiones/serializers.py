from rest_framework import serializers

from .models import Sesion


class SesionSerializer(serializers.ModelSerializer):
    room_name = serializers.UUIDField(read_only=True)

    class Meta:
        model = Sesion
        fields = ["id", "entrevista", "creada_por", "room_name", "estado", "fecha_inicio", "fecha_fin"]
        read_only_fields = ["id", "room_name", "fecha_inicio"]


class CrearSesionSerializer(serializers.Serializer):
    entrevista_id = serializers.IntegerField()
    creada_por = serializers.IntegerField()
