from django.contrib import admin
from .models import Reporte

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ['entrevista', 'participante', 'nivel_riesgo', 'fecha_creacion']  # type: ignore
    list_filter = ('nivel_riesgo',)
    search_fields = ('resumen',)
