import json
from django.core.serializers import serialize
from typing import Any,Dict
from django.shortcuts import redirect, render
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse, JsonResponse
from cursos.models import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# class ListarUsuarios(ListView):
#     model = Usuario
#     template_name = 'usuarios/index.html'
#     context_object_name = 'usuarios'
    
#     def get(self, request,  *args, **kwargs):
#         usuarios = Usuario.object.filter(nombre__contains = request.GET.get('search', ''))
#         context = {
#             'usuarios': usuarios
#         }
#         return render(request, 'usuarios/index.html', context)
class DetalleUsuario(DetailView):
    model= Usuario
    template_name = 'usuarios/detalle.html'
    context_object_name= 'usuario'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cursos'] = DetallesCursos.objects.filter(alumno_id=int(self.kwargs['pk']))
        return context

class CreateUsuario(CreateView):
    model = Usuario
    form_class = UsuariosForm
    template_name = 'usuarios/create.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name,{'form':form})
        print(form.cleaned_data.get('groups'))
        nuevo_usuario = Usuario(
            username = form.cleaned_data.get('username'),
            nombre = form.cleaned_data.get('nombre'),
            apellido = form.cleaned_data.get('apellido'),
            email = form.cleaned_data.get('email'),
            direccion = form.cleaned_data.get('direccion'),
            c_id = form.cleaned_data.get('c_id'),
            telefono = form.cleaned_data.get('telefono'),
        )
        groups = form.cleaned_data.get('groups')
        if request.FILES != {}:
            nuevo_usuario.foto = request.FILES['foto']
        nuevo_usuario.set_password(form.cleaned_data.get('password'))
        nuevo_usuario.save()
        for g in groups:
            nuevo_usuario.groups.add(g)
        return redirect('index')
    
# class ActualizarUsuario(UpdateView):
#     model = Usuario
#     form_class = UsuariosForm
#     template_name = 'usuarios/actualizar.html'
#     success_url = reverse_lazy('usuario')

# class EliminarUsuario(DeleteView):
#     model = Usuario
#     template_name = 'Control/usuario_confirm_delete.html'
#     success_url = reverse_lazy('usuario')

#     def delete(self, request, *args, **kwargs):
#         if is_ajax(request=self.request):
#             return reverse_lazy('usuario')
#         self.object = self.get_object()
#         self.object.delete()
#         mensaje = f'La orden {self.model.id} eliminado correctamente'
#         return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

