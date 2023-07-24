from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

class CreateOrden(CreateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'ordenes/create.html'