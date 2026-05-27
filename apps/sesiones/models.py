import uuid

from django.db import models


class Sesion(models.Model):
    class Estado(models.TextChoices):
        ACTIVA = "activa", "Activa (preparación)"
        INICIADA = "iniciada", "Iniciada (en curso)"
        FINALIZADA = "finalizada", "Finalizada"

    entrevista = models.ForeignKey(
        "entrevistas.Entrevista",
        on_delete=models.CASCADE,
        related_name="sesiones",
    )
    creada_por = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.PROTECT,
        related_name="sesiones_creadas",
    )
    room_name = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.ACTIVA,
    )
    observaciones_internas = models.TextField(
        blank=True,
        null=True,
        help_text="Observaciones internas del evaluador",
    )
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-fecha_inicio"]
        verbose_name = "Sesión"
        verbose_name_plural = "Sesiones"

    def __str__(self):
        return f"Sesión {self.room_name} - {self.entrevista}"
