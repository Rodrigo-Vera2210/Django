from django.urls import path
from .views import *

urlpatterns = [
    path('',ListarCursos.as_view(), name="cursos"),
    path('crear/',CreateCursos.as_view(), name="createCursos"),
    path('view/<int:pk> <int:clase>',DetalleCursos.as_view(), name="detalleCursos"),
    path('intro/<int:pk>',IntroCursos.as_view(), name="introCursos"),
    path('delete/<int:pk>',EliminarCurso.as_view(), name="eliminarCursos"),
]
