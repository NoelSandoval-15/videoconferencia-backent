from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CrearObtenerSesionView, FinalizarSesionView, SesionViewSet

router = DefaultRouter()
router.register(r"", SesionViewSet, basename="sesion")

urlpatterns = [
    path("", include(router.urls)),
    path("crear/", CrearObtenerSesionView.as_view(), name="sesiones-crear"),
    path("<int:entrevista_id>/", CrearObtenerSesionView.as_view(), name="sesiones-obtener"),
    path("<int:sesion_id>/finalizar/", FinalizarSesionView.as_view(), name="sesiones-finalizar"),
]
