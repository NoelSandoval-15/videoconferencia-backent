from rest_framework.viewsets import ModelViewSet

from .models import Prueba, PruebaEntrevista
from .serializers import PruebaEntrevistaSerializer, PruebaSerializer


class PruebaViewSet(ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer


class PruebaEntrevistaViewSet(ModelViewSet):
    queryset = PruebaEntrevista.objects.all()
    serializer_class = PruebaEntrevistaSerializer
