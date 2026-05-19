from django.contrib import admin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido", "email", "rol", "estado")
    list_filter = ("rol", "estado")
    search_fields = ("nombre", "apellido", "email")
