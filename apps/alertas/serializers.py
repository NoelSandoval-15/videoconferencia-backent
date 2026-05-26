from rest_framework import serializers
from .models import Alerta

class AlertaSerializer(serializers.ModelSerializer):
    id_entrevista = serializers.CharField(write_only=True, required=False)
    id_participante = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Alerta
        fields = '__all__'
        read_only_fields = ['fecha_creacion', 'entrevista', 'participante']

    def create(self, validated_data):
        id_entrevista = validated_data.pop("id_entrevista", None)
        id_participante = validated_data.pop("id_participante", None)

        from apps.entrevistas.models import Entrevista
        from apps.usuarios.models import Usuario

        # Usar la primera entrevista y usuario disponibles como mock para desarrollo local
        entrevista = Entrevista.objects.first()
        usuario = Usuario.objects.first()

        validated_data["entrevista"] = entrevista
        validated_data["participante"] = usuario

        return Alerta.objects.create(**validated_data)
