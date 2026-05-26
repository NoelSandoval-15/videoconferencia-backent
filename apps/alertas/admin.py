from django.contrib import admin
from .models import Alerta

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ['tipo_alerta', 'severidad', 'entrevista', 'participante', 'timestamp_alerta', 'fecha_creacion']  # type: ignore
    list_filter = ('severidad', 'tipo_alerta')
    search_fields = ('tipo_alerta', 'descripcion')
