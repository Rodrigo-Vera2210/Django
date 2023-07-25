from django.db import models

class Cliente(models.Model):
    nombres = models.CharField(max_length=50, blank=False, null=False)
    cedula = models.IntegerField(max_length=10, null=False, blank=False)
    ruc = models.IntegerField(max_length=13, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombres
