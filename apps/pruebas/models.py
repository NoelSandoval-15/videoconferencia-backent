from django.db import models


class Prueba(models.Model):
    class Tipo(models.TextChoices):
        TEORICA = "teorica", "Teórica"
        TECNICA = "tecnica", "Técnica"
        MIXTA = "mixta", "Mixta"

    class Area(models.TextChoices):
        PROGRAMACION = "programacion", "Programación"
        NEGOCIO = "negocio", "Negocio"
        JURIDICA = "juridica", "Jurídica"

    class Nivel(models.TextChoices):
        BASICO = "basico", "Básico"
        INTERMEDIO = "intermedio", "Intermedio"
        AVANZADO = "avanzado", "Avanzado"

    class Estado(models.TextChoices):
        BORRADOR = "borrador", "Borrador"
        ACTIVA = "activa", "Activa"
        INACTIVA = "inactiva", "Inactiva"
        ARCHIVADA = "archivada", "Archivada"

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    creada_por = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.PROTECT,
        related_name="pruebas_creadas",
    )
    tipo = models.CharField(max_length=30, choices=Tipo.choices)
    area = models.CharField(max_length=30, choices=Area.choices)
    nivel = models.CharField(max_length=30, choices=Nivel.choices)
    duracion_minutos = models.PositiveIntegerField()
    puntaje_maximo = models.PositiveIntegerField(default=100)
    estado = models.CharField(
        max_length=30,
        choices=Estado.choices,
        default=Estado.BORRADOR,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"

    def __str__(self):
        return self.titulo


class PruebaEntrevista(models.Model):
    class Estado(models.TextChoices):
        ASIGNADA = "asignada", "Asignada"
        INACTIVA = "inactiva", "Inactiva"
        CANCELADA = "cancelada", "Cancelada"

    entrevista = models.ForeignKey(
        "entrevistas.Entrevista",
        on_delete=models.CASCADE,
        related_name="pruebas_asignadas",
    )
    prueba = models.ForeignKey(
        "pruebas.Prueba",
        on_delete=models.PROTECT,
        related_name="entrevistas_asignadas",
    )
    asignada_por = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.PROTECT,
        related_name="pruebas_entrevista_asignadas",
    )
    estado = models.CharField(
        max_length=30,
        choices=Estado.choices,
        default=Estado.ASIGNADA,
    )
    observaciones = models.TextField(blank=True, null=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-fecha_asignacion"]
        constraints = [
            models.UniqueConstraint(
                fields=["entrevista", "prueba"],
                name="prueba_unica_por_entrevista",
            )
        ]
        verbose_name = "Prueba de entrevista"
        verbose_name_plural = "Pruebas de entrevista"

    def __str__(self):
        return f"{self.entrevista} - {self.prueba}"
