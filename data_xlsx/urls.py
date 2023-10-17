from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    # Importante no colocar el / en la ruta subir-data-xlsx/ debe ser asi: subir-data-xlsx
    path('subir-data-xlsx', views.cargar_archivo, name="cargar_archivo"),

    path('data-demo/', views.data_demo, name='data_demo'),
]
