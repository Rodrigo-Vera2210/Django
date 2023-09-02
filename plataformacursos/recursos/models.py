from django.db import models
from clases.models import *

class Recursos(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(max_length=200)
    link = models.URLField(max_length=200, null=False, blank=False)
    precio = models.DecimalField(max_digits=12,decimal_places=2,default=0.0)
    clase = models.ForeignKey(Clases, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

