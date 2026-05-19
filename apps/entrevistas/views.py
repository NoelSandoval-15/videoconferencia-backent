from rest_framework.viewsets import ModelViewSet

from .models import Entrevista
from .serializers import EntrevistaSerializer


class EntrevistaViewSet(ModelViewSet):
    queryset = Entrevista.objects.all()
    serializer_class = EntrevistaSerializer
