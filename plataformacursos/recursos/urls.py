from django.urls import path
from .views import *

urlpatterns = [
    path('crear/',CreateRecursos.as_view(), name="createRecursos")
]
