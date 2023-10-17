from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('subir-data-xlsx/', views.cargar_archivo, name="cargar_archivo"),

    path('data-demo/', views.data_demo, name='data_demo'),
]
