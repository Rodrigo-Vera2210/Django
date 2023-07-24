from django.forms import ModelForm
from .models import *

class ServiciosForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'