from django.db import models


class Entrevista(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = "borrador", "Borrador"
        PROGRAMADA = "programada", "Programada"
        EN_PROCESO = "en_proceso", "En proceso"
        FINALIZADA = "finalizada", "Finalizada"
        CANCELADA = "cancelada", "Cancelada"

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    creada_por = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.PROTECT,
        related_name="entrevistas_creadas",
    )
    estado = models.CharField(
        max_length=30,
        choices=Estado.choices,
        default=Estado.BORRADOR,
    )
    fecha_programada = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "Entrevista"
        verbose_name_plural = "Entrevistas"

    def __str__(self):
        return self.titulo
