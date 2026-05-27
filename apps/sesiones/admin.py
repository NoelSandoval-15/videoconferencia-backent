from django.contrib import admin

from .models import Sesion


@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ["id", "entrevista", "creada_por", "room_name", "estado", "fecha_inicio", "fecha_fin"]
    list_filter = ["estado", "fecha_inicio"]
    search_fields = ["entrevista__titulo", "room_name"]
    readonly_fields = ["room_name", "fecha_inicio", "fecha_actualizacion"]
    fieldsets = (
        ("Información de la Sesión", {
            "fields": ("entrevista", "creada_por", "room_name", "estado")
        }),
        ("Fechas", {
            "fields": ("fecha_inicio", "fecha_fin", "fecha_actualizacion")
        }),
        ("Observaciones", {
            "fields": ("observaciones_internas",),
            "classes": ("wide",)
        }),
    )
