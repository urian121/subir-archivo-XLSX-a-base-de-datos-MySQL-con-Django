from django.shortcuts import render

import pandas as pd
from .models import DatosXLSX
from django.http import JsonResponse

#  Usando la librería pandas para leer el archivo XLSX y guardar los datos en la base de datos.


def inicio(request):
    return render(request, 'index.html')


def cargar_archivo(request):
    try:
        if request.method == 'POST':
            archivo_xlsx = request.FILES['archivo_xlsx']
            if archivo_xlsx.name.endswith('.xlsx'):
                df = pd.read_excel(archivo_xlsx, header=0)
                for _, row in df.iterrows():
                    cedula = row['Cedula']
                    nombre = row['Nombre']
                    email = row['Email']
                    edad = row['Edad']
                    telefono = row['Telefono']

                    """ 
                    El método update_or_create en Django se utiliza para buscar un registro en una tabla de base de datos y, 
                    si lo encuentra, lo actualiza con nuevos valores. Si no se encuentra un registro con las condiciones de 
                    búsqueda especificadas, se crea un nuevo registro con los valores proporcionados.
                    """
                    empleado, creado = DatosXLSX.objects.update_or_create(
                        cedula=cedula,
                        defaults={
                            'nombre': nombre,
                            'email': email,
                            'edad': edad,
                            'telefono': telefono,
                        }
                    )

                return JsonResponse({'status_server': 'success', 'message': 'Felicitaciones, la data fue importada correctamente 😉'})
            else:
                return JsonResponse({'status_server': 'error', 'message': 'El archivo debe ser un archivo de Excel válido.'})
        else:
            return render(request, 'index.html')

    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
        return JsonResponse({'status_server': 'error', 'message': 'Error interno del servidor.'})
