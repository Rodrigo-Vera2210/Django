from django.forms import ModelForm
from cursos.models import *

class CursosForm(ModelForm):
    class Meta:
        model = Cursos
        fields = '__all__'

class DetalleCursosForm(ModelForm):
    class Meta:
        model = DetallesCursos
        fields = '__all__'
