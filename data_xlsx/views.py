from django.shortcuts import render

#  Usando la librería pandas para leer el archivo XLSX y guardar los datos en la base de datos.
import pandas as pd
from .models import DatosXLSX
from django.http import JsonResponse


def inicio(request):
    return render(request, 'index.html')


def cargar_archivo(request):
    try:
        if request.method == 'POST':
            # Se procede a obtener el archivo XLSX enviado en el formulario, atraves del request.FILES['archivo_xlsx']
            # 'archivo_xlsx' es el nombre del campo en el formulario que se espera contenga el archivo
            archivo_xlsx = request.FILES['archivo_xlsx']

            # Se verifica si el nombre del archivo tiene la extensión ".xlsx".
            # Si no es así, se responde con un mensaje de error, indicando que el archivo debe ser un archivo de Excel válido.
            if archivo_xlsx.name.endswith('.xlsx'):

                # Si el archivo es válido, se utiliza la biblioteca Pandas (importada como pd)
                # para leer el contenido del archivo XLSX y cargarlo en un DataFrame llamado df.
                df = pd.read_excel(archivo_xlsx, header=0)
                # Los datos del archivo se leen asumiendo que la primera fila contiene los nombres de las columnas (encabezados).

                # Se itera sobre cada fila del DataFrame df para obtener los valores de las columnas
                # "Cedula", "Nombre", "Email", "Edad" y "Telefono" de cada fila.
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


def data_demo(request):
    # Crear un diccionario de datos
    data = {
        'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
        'Edad': [25, 30, 35, 40],
        'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston']
    }

    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame(data)

    # Imprimir el DataFrame
    print(df)

    # Crear una lista para almacenar los datos de cada fila
    data_list = []

    for index, row in df.iterrows():
        nombre = row['Nombre']
        edad = row['Edad']
        ciudad = row['Ciudad']
        print(f'Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}')

        data_list.append({'Nombre': nombre, 'Edad': edad, 'Ciudad': ciudad})
    # Convertir la lista en un objeto JSON y retornarlo
    return JsonResponse({'result': data_list})
