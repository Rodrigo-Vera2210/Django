from django.urls import path
from . import views

urlpatterns = [
    path('', views.sumatoriaCarrito, name='sumatoriaCarrito'),
    path('add/', views.carritoAdd, name='carritoAdd'),
    path('delete/', views.carritoDelete, name='carritoDelete'),
]
