import json
from typing import Any, Dict
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import *
from .models import *
from clases.models import *
from recursos.models import *
from .forms import *
from usuarios.forms import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class ListarCursos(ListView):
    model: Cursos
    template_name = 'cursos/index.html'

    def get(self, request,  *args, **kwargs):
        cursos = Cursos.objects.filter(titulo__contains = request.GET.get('search', ''))
        context = {
            'cursos': cursos,
            'detallescursos': DetallesCursos.objects.filter(alumno_id = request.user.id)
        }
        return render(request, self.template_name, context)
    
class CreateCursos(CreateView):
    model = Cursos
    form_class = CursosForm
    template_name = 'cursos/create.html'
    success_url = reverse_lazy('cursos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clases"] = Clases.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        if is_ajax(request=self.request):
            if request.POST['accion'] == 'guardar':
                try:
                    print(request.POST)
                    curso = Cursos()
                    curso.portada = request.FILES['portada']
                    curso.titulo = request.POST['titulo']
                    curso.descripcion = request.POST['descripcion']
                    curso.precio = request.POST['precio']
                    curso.profesor_id = request.POST['profesor']
                    curso.fechaInicio = request.POST['fechaInicio']
                    curso.fechaFinal = request.POST['fechaFinal']
                    curso.horario = request.POST['horario']
                    print(curso)
                    curso.save()
                    modulos = json.loads(request.POST['modulos'])
                    clases = json.loads(request.POST['clases'])
                    for x in modulos:
                        modulo = Modulo()
                        mod = json.loads(json.dumps(modulos[x]))
                        modulo.curso_id = curso.id
                        modulo.titulo = mod['titulo']
                        modulo.descripcion = mod['descripcion']
                        modulo.save()
                        for y in clases[x]:
                            detModulo = DetalleModulo()
                            detModulo.modulo_id = modulo.id
                            detModulo.clase_id = y
                            detModulo.save()
                    data['error']=''
                except Exception as e:
                    data['error'] = str(e)
            elif request.POST['accion'] == 'inscripcionCurso':
                try:
                    detalleCursos = DetallesCursos.objects.filter(alumno_id = int(request.POST['user'])).filter(curso_id = request.POST['id'])
                    if(len(detalleCursos) == 0):
                        detalleC = DetallesCursos()
                        detalleC.alumno_id = int(request.POST['user'])
                        detalleC.curso_id = int(request.POST['id'])
                        detalleC.inscripcion = True
                        detalleC.save()
                        data['error']=''
                    else:
                        data['error']='Ya esta inscripto'
                except Exception as e:
                    print(e)
                    data['error'] = str(e)
            return JsonResponse(data)
        
class DetalleCursos(DetailView):
    model = Cursos
    template_name = 'cursos/curso.html'

    
    def get(self, request, *args, **kwargs):
        if(kwargs['clase'] != 0):
            if(request.user.is_authenticated == False):
                return render(request, 'index.html',{})
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if is_ajax(request=self.request) and request.POST['action'] == 'guardarRecurso':
            data = {}
            try:
                recurso = Recursos()
                recurso.titulo = request.POST['titulo']
                recurso.descripcion = request.POST['descripcion']
                recurso.link = request.POST['link']
                recurso.precio = float(request.POST['precio'])
                recurso.clase_id = int(request.POST['clase'])
                recurso.save()
                data['error']=''
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['modulos'] = Modulo.objects.filter(curso_id = self.get_object().id)
        context['detallesModulos'] =  DetalleModulo.objects.filter(curso_id = self.get_object().id)
        print(self.kwargs['clase'])
        if self.kwargs['clase'] == 0:
            context['clase'] = Clases.objects.get(id = context['detallesModulos'][0].clase.id)
            context['recursos'] = ''
        else:
            context['clase'] = Clases.objects.get(id = self.kwargs['clase'])
            context['recursos'] = Recursos.objects.filter(clase_id = self.kwargs['clase'])
        return context

class IntroCursos(DetailView):
    model = Cursos
    template_name = 'cursos/intro.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['modulos'] = Modulo.objects.filter(curso_id = self.get_object().id)
        return context



class EliminarCurso(DeleteView):
    model = Cursos
    template_name = 'delete/cursos_delete.html'
    success_url= '../../cursos'

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('cursos')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})


