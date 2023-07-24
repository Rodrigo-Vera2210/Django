from django.urls import path,include
from .views import *

urlpatterns = [
    path('',ListaProductos.as_view(),name='productos'),
]