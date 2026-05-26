from django.db import models

class Reporte(models.Model):
    entrevista = models.ForeignKey(
        "entrevistas.Entrevista",
        on_delete=models.CASCADE,
        related_name="reportes",
    )
    participante = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.CASCADE,
        related_name="reportes",
    )
    nivel_riesgo = models.CharField(max_length=50)
    resumen_general = models.TextField(blank=True, null=True)
    resumen_participante = models.TextField(blank=True, null=True)
    recomendaciones = models.TextField(blank=True, null=True)
    puntaje_atencion = models.IntegerField(default=100)
    puntaje_sospecha = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()

    def __str__(self):
        return f"Reporte - {self.entrevista} ({self.fecha_creacion})"
