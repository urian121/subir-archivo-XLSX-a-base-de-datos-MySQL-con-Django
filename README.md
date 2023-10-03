### Cargar Archivo XLSX a Base de Datos MySQL con Django

1.  Crear un entorno virtual, hay muchas formas

        Opción 1: Crear entorno virtual con el paquete virtualenv
        Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
        pip install virtualenv ->Instalar de forma global
        virtualenv env ->Crear entorno
        virtualenv --version ->Ver la versión de virtualenv

        Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
        python -m venv env

2.  Activar entorno virtual

        . env/Script/activate ->para Windows
        . env/bin/activate -> Para Mac
        deactivate -->Para desactivar mi entorno virtual

3.  Instalar Djando desde el manejador de paquete de Python Pip, ya dentro del entorno virtual.

        python -m pip install Django
        pip install Django
        Nota: para instalar Django en una version especifica
        pip install Django==4.2.4

4.  Instalar Driver para conectar Gestor de BD MySQL con Django

        pip install mysqlclient

5.  Instalar la libreria pandas y la libreria openpyxl

        pip install pandas
        pip install openpyxl

6.  Crear el proyecto con Djando

        `django-admin startproject project_core .`
        El punto . es crucial le dice al script que instale Django en el directorio actual

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

7.  Crear una aplicación en Django

        python manage.py startapp data_xlsx

8.  Instalar nuestra aplicación (empleados) ya creada en el proyecto en el archivo settings.py del proyecto

        archivo settings.py
        INSTALLED_APPS = [
                ----,
                'empleados',
        ]

9.  Crear la Base de datos en MySQL (bd_empleados)
10. Editar el archivo settings.py del proyecto, cambiando los parametros de conexión a MySQL

        `
        DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.mysql', #ENGINE es motor de BD
                        'NAME': 'bd_empleados',
                        'USER': 'root',
                        'PASSWORD': '',
                        'HOST': '127.0.0.1',
                        'PORT': '3306',
                }
        }
        `

11. Crear una clase en models.py la cual reprtesentara mi tabla en BD,(empleados) preferiblemente los modelos
    se declaran en singular

        class DatosXLSX(models.Model):
                nombre = models.CharField(max_length=255)
                cedula = models.CharField(max_length=15, null=True)
                email = models.EmailField(max_length=50)
                edad = models.IntegerField()
                telefono = models.CharField(max_length=20)

                class Meta:
                        db_table = 'empleados'

12. Crear las migraciones que estan en mi modelo

        python manage.py makemigrations empleados

13. Correr migraciones

        python manage.py migrate

14. Crear el archivo urls.py de mi aplicacion y definir algunas urls

        from django.urls import path
        from . import views

        urlpatterns = [
                path('', views.inicio, name="inicio"),
                path('subir-data-xlsx', views.cargar_archivo, name="cargar_archivo"),
        ]

15. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto

        from django.urls import path, include
        urlpatterns = [
                path('admin/', admin.site.urls),
                path("", include("data_xlsx.urls")),
        ]

16. Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000

17. Crear la carpeta 'templates' dentro de la aplicación donde estarán mis archivos.html

18. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

19. Instalar todo los paquetes del proyecto
    pip install -r requirements.txt

### Resultado Final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/Cargar%20Archivo%20XLSX%20-%20urian%20viera.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
