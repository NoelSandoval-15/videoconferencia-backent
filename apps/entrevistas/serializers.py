from rest_framework import serializers

from .models import Entrevista

"este es el serializer de la app entrevistas"

class EntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrevista
        fields = "__all__"
