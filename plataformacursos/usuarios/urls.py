from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import *

urlpatterns = [
    # path('',login_required(Listarmpleados.as_view()), name='empleado'),
    path('crear/',CreateUsuario.as_view(), name='usuarioCreate'),
    path('update/<int:pk>',DetalleUsuario.as_view(), name='usuarioDetalle'),
    # path('update/<int:pk>',Actualizarmpleado.as_view(), name='empleado_update'),
    # path('delete/<int:pk>',login_required(EliminarEmpleado.as_view()), name='empleado_delete'),
]