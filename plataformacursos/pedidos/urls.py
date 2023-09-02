from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(ListarPedidos.as_view()), name="pedidos"),
    path('crear/',login_required(CreatePedidos.as_view()), name="createPedidos"),
    path('detalle/<int:pk>',login_required(DetallePedidos.as_view()), name="detallePedidos"),
    path('delete/<int:pk>',login_required(EliminarPedido.as_view()), name='deletePedidos'),
    path('mispedidos/<int:pk>',login_required(ListarMisPedidos.as_view()), name="misPedidos")
]
