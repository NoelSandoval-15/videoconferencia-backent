from django.db import models


class Usuario(models.Model):
    class Rol(models.TextChoices):
        SUPERVISOR = "supervisor", "Supervisor"
        INVITADO = "invitado", "Invitado"

    class Estado(models.TextChoices):
        ACTIVO = "activo", "Activo"
        INACTIVO = "inactivo", "Inactivo"

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    rol = models.CharField(max_length=30, choices=Rol.choices)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.ACTIVO,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre", "apellido"]
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_rol_display()}"
