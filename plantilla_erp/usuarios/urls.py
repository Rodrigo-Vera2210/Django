from django.urls import path,include
from .views import *

urlpatterns = [
    path('',ListaUsuarios.as_view(),name='usuarios'),
]