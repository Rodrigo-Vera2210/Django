from django.db import models
from cursos.models import *
from embed_video.fields import EmbedVideoField

class Modulo(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(max_length=200)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'

class Clases(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(max_length=200)
    link_video = EmbedVideoField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'


class DetalleModulo(models.Model):
    modulo= models.ForeignKey(Modulo, on_delete=models.CASCADE)
    clase= models.ForeignKey(Clases, on_delete=models.CASCADE)
    curso= models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.modulo)