from django.db import models
from usuarios.models import *
from cursos.models import Cursos
from recursos.models import *

class Pedidos(models.Model):
    comprobante = models.FileField('comprobante', upload_to='comprobantes/',max_length=255,null=True, blank=True)
    total = models.DecimalField(max_digits=12,decimal_places=2,default=0.0)
    aprobado = models.BooleanField(default=False)
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.today())

    def __str__(self):
        return str(self.id)

class DetallePedidosCursos(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    aprobacion = models.BooleanField(default=False)

    def __str__(self):
        return self # TODO
    
class DetallePedidosRecursos(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recursos, on_delete=models.CASCADE)
    aprobacion = models.BooleanField(default=False)

    def __str__(self):
        return self # TODO