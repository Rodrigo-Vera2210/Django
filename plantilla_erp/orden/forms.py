from django.forms import ModelForm
from .models import *

class DetalleProductoForm(ModelForm):
    class Meta:
        model = DetalleProducto
        fields = '__all__'

class DetalleServicioForm(ModelForm):
    class Meta:
        model = DetalleServicio
        fields = '__all__'

class OrdenForm(ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'