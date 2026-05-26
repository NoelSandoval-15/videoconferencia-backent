from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Alerta
from .serializers import AlertaSerializer
from django.conf import settings
import os

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all().order_by('-fecha_creacion')
    serializer_class = AlertaSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        # Validate API Key from header
        auth_header = request.headers.get('Authorization')
        expected_api_key = getattr(settings, 'DJANGO_API_KEY', 'dev-api-key')
        if not auth_header or auth_header != f"Api-Key {expected_api_key}":
            return Response({"detail": "Invalid or missing API Key"}, status=status.HTTP_401_UNAUTHORIZED)
            
        return super().create(request, *args, **kwargs)
