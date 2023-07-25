from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

class ListaProductos(ListView):
    model = Producto
    template_name = 'productos/index.html'
    context_object_name = 'productos'