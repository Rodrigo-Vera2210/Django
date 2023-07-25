from django.db import models

class Usuarios(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombres # TODO
