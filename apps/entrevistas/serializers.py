from rest_framework import serializers

from .models import Entrevista


class EntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrevista
        fields = "__all__"
