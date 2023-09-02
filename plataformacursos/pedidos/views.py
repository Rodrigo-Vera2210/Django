import json
from typing import Any, Dict
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy,reverse
from django.views.generic import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class CreatePedidos(CreateView):
    model = Pedidos
    form_class = PedidosForm
    template_name = 'pedidos/create.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        data = {}
        if is_ajax(request=self.request):
            if request.POST['accion'] == 'guardar':
                try:
                    pedido = Pedidos()
                    pedido.comprobante = request.FILES['comprobante']
                    pedido.total = float(request.POST['total'])
                    pedido.alumno_id = int(request.POST['alumno'])
                    pedido.save()
                    cursos = json.loads(request.POST['cursos'])
                    for x in cursos:
                        detCurso = DetallePedidosCursos()
                        detCurso.pedido_id = pedido.id
                        detCurso.alumno_id = int(request.POST['alumno'])
                        detCurso.curso_id = int(x)
                        detCurso.save()
                    data['error'] = ''
                except Exception as e:
                    print(e)
                    data['error'] = str(e)
            if request.POST['accion'] == 'aprobar':
                try:
                    print(request.POST)
                    pedido = Pedidos.objects.get(id = int(request.POST['id']))
                    idAlumno = pedido.alumno.id
                    detallePCursos = DetallePedidosCursos.objects.filter(alumno_id = idAlumno).filter(pedido_id = pedido.id)
                    pedido.aprobado = True
                    pedido.save()
                    for detpcursos in detallePCursos:
                        detpcursos.aprobacion = True
                        detpcursos.save()
                        detcursos = DetallesCursos.objects.filter(curso_id = detpcursos.curso_id).filter(alumno_id = idAlumno)
                        for detcurso in detcursos:
                            detcurso.aprobacion = True
                            detcurso.save()
                    data['error']=''
                except Exception as e:
                    print(e)
                    data['error'] = str(e)
            
            return JsonResponse(data)

class ListarPedidos(ListView):
    model=Pedidos
    template_name = 'pedidos/index.html'
    context_object_name= 'pedidos'

class ListarMisPedidos(ListView):
    model=Pedidos
    template_name = 'pedidos/mispedidos.html'
    context_object_name= 'pedidos'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['pedidos'] = Pedidos.objects.filter(alumno_id=int(self.kwargs['pk']))
        return context

class DetallePedidos(DetailView):
    model = Pedidos
    template_name = 'pedidos/detalle.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cursos'] = DetallePedidosCursos.objects.filter(pedido_id = self.get_object().id)
        context['recursos'] = DetallePedidosRecursos.objects.filter(pedido_id = self.get_object().id)
        return context
    
class EliminarPedido(DeleteView):
    model = Pedidos
    template_name = 'delete/pedidos_delete.html'
    success_url= '../../pedidos'


    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('pedidos')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'El pedido {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': ''})