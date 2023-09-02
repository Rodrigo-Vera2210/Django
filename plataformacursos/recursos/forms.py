from django.forms import ModelForm
from recursos.models import *

class RecursosForm(ModelForm):
    class Meta:
        model = Recursos
        fields = '__all__'
