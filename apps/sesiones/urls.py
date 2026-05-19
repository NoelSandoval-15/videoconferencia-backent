from django.urls import path

from .views import CrearObtenerSesionView, FinalizarSesionView

urlpatterns = [
    path("", CrearObtenerSesionView.as_view(), name="sesiones-crear"),
    path("<int:entrevista_id>/", CrearObtenerSesionView.as_view(), name="sesiones-obtener"),
    path("<int:sesion_id>/finalizar/", FinalizarSesionView.as_view(), name="sesiones-finalizar"),
]
