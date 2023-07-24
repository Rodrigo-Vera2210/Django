from django.urls import path,include
from .views import *

urlpatterns = [
    path('', CreateOrden.as_view(), name = 'create_orden'),
]