from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class CreateClases(CreateView):
    model = Clases
    form_class = ClasesForm
    template_name = 'clases/create.html'
    success_url = reverse_lazy('clases')

    def post(self, request: HttpRequest, *args, **kwargs):
        data = {}
        if request.POST['accion']=='guardar':
            try:
                clase = Clases()
                clase.titulo = request.POST['titulo']
                clase.descripcion = request.POST['descripcion']
                clase.link_video = request.POST['link_video']
                clase.save()
                data['error']=''
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)

class ListarClases(ListView):
    model: Clases
    template_name = 'clases/index.html'

    def get(self, request,  *args, **kwargs):
        clases = Clases.objects.filter(titulo__contains = request.GET.get('search', ''))
        context = {
            'clases': clases,
        }
        return render(request, self.template_name, context)

class EliminarClase(DeleteView):
    model = Clases
    template_name = 'delete/clases_delete.html'
    success_url= '../../clases'

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('clases')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': ''})

class CreateModulo(CreateView):
    model = Modulo
    form_class = ModuloForm
    template_name = 'modulos/create.html'
    success_url = reverse_lazy('index')