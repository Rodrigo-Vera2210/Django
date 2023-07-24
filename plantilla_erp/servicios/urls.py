from django.urls import path,include
from .views import *

urlpatterns = [
    path('',ListaServicios.as_view(),name='servicios'),
]