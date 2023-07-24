from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

class ListaClientes(ListView):
    model = Cliente
    template_name = 'clientes/index.html'