from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

class ListaServicios(ListView):
    model = Servicio
    template_name = 'servicios/index.html'
    context_object_name = 'servicios'