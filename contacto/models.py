from django.db import models
from datetime import date

class Contacto(models.Model):

    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    compania = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(default=date.today)
    nota = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.nombre

