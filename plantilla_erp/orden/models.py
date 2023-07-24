from django.db import models
from clientes.models import *
from productos.models import *
from servicios.models import *
from usuarios.models import *

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    iva = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    total = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    aprobacion = models.BooleanField()

    def __str__(self):
        return self # TODO
    
class DetalleServicio(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField(max_length=10, blank=False, null=False)
    precio_unitario = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    total = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    orden = models.ForeignKey(Orden, models.CASCADE)
    
    def __str__(self):
        return self # TODO

class DetalleProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(max_length=10, blank=False, null=False)
    precio_unitario = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    total = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    orden = models.ForeignKey(Orden, models.CASCADE)

    def __str__(self):
        return self # TODO
    


