from django.forms import *
from .models import *

class PedidosForm(ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__'