from django.contrib import admin

from .models import Entrevista


@admin.register(Entrevista)
class EntrevistaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "creada_por", "estado", "fecha_programada")
    list_filter = ("estado",)
    search_fields = ("titulo", "descripcion", "creada_por__nombre", "creada_por__email")
