from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

class ListaUsuarios(ListView):
    model = Usuarios
    template_name = 'usuarios/index.html'
    context_object_name = 'usuarios'