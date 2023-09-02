from django.forms import *
from clases.models import *

class ClasesForm(ModelForm):
    class Meta:
        model = Clases
        fields = '__all__'

class ModuloForm(ModelForm):
    class Meta:
        model = Modulo
        fields = '__all__'