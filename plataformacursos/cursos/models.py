from django.db import models
from usuarios.models import *

class Cursos(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=12,decimal_places=2,default=0.0)
    portada = models.ImageField('Portada', upload_to='cursos/',max_length=255,null=True, blank=True)
    fechaInicio = models.DateField('Fecha de inicio', default=datetime.today())
    fechaFinal = models.DateField('Fecha de finalización',default=datetime.today())
    horario = models.CharField(max_length=100, null=False, blank=False, default='Lunes y Jueves de 19:00 a 21:00')
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class DetallesCursos(models.Model):
    progreso = models.IntegerField(default=0)
    nota = models.IntegerField(default=0)
    inscripcion = models.BooleanField(default=False)
    aprobacion = models.BooleanField(default=False) 
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self
    
    class Meta:
        verbose_name = 'Detalle Curso'
        verbose_name_plural = 'Detalle Cursos'
