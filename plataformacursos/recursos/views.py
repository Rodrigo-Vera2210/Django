from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

class CreateRecursos(CreateView):
    model = Recursos
    form_class = RecursosForm
    template_name = 'recursos/create.html'
    success_url = reverse_lazy('recursos')

