from django.db import models
from datetime import date

class Todo(models.Model):

    titulo = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    fecha = models.DateField(default=date.today)
    fecha_estimada = models.DateField(blank=True, null=True)
    prioridad = models.IntegerField(default=3)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.titulo
