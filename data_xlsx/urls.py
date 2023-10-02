from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargar_archivo, name="cargar_archivo"),
]
