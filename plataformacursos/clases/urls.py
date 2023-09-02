from django.urls import path
from .views import *

urlpatterns = [
    path('',ListarClases.as_view(), name="clases"),
    path('crear/',CreateClases.as_view(), name="createClases"),
    path('delete/<int:pk>/',EliminarClase.as_view(), name="eliminarClases"),
    path('modulo/crear/',CreateModulo.as_view(), name="createModulo"),
]
