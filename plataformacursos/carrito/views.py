from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .carrito import *
from cursos.models import *
from recursos.models import *

def sumatoriaCarrito(request):
    carrito = Carrito(request)
    
    return render(request, 'carrito/index.html', {'carrito2': carrito})

def carritoAdd(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'addCurso':
        if request.POST.get('tipo') == 'curso':
            cursoId = int(request.POST['id'])
            curso = get_object_or_404(Cursos, id=cursoId)
            carrito.add(product=curso,tipo="cursos")
        elif request.POST.get('tipo') == 'recurso':
            recursoId = int(request.POST['id'])
            recurso = get_object_or_404(Recursos, id=recursoId)
            carrito.add(product=recurso,tipo="recursos")
        cantidad = carrito.__len__()
        reponse = JsonResponse({'cant':cantidad,'error':''})
        return reponse
    
def carritoDelete(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'deleteCurso':
        cursoId = int(request.POST['id'])
        carrito.delete(productId=cursoId,tipo=request.POST['tipo'])
        response = JsonResponse({'error':''})
        return response