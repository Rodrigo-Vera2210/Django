from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    precio = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.nombre
