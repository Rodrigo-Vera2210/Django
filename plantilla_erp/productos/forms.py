from django.forms import ModelForm
from .models import *

class ProveedoresForm(ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'