from django.db import models

# Create your models here.
from django.db import models


class DatosXLSX(models.Model):
    nombre = models.CharField(max_length=255)
    cedula = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)

    class Meta:
        db_table = 'empleados'
