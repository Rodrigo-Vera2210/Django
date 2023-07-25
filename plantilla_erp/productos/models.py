from django.db import models

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    ruc = models.IntegerField(max_length=13, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.IntegerField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nombre # TODO
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    marca = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(null=False, blank=False)
    precio = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedores = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
