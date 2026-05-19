from rest_framework import serializers

from .models import Prueba, PruebaEntrevista


class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = "__all__"


class PruebaEntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaEntrevista
        fields = "__all__"
