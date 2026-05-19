from django.contrib import admin

from .models import Sesion


@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ["id", "entrevista", "creada_por", "room_name", "estado", "fecha_inicio", "fecha_fin"]
    list_filter = ["estado"]
    search_fields = ["entrevista__titulo", "room_name"]
