from django.db import models

# Create your models here.

class Condicionales(models.Model):
    tipo = models.CharField(max_length=20,primary_key=True)
    Codigo = models.CharField(max_length=1)
    Nombre = models.CharField(max_length=1)
    Precio = models.CharField(max_length=1)
    Porcentaje = models.FloatField()
    Inicio = models.CharField(max_length=2)
    Extension = models.CharField(max_length=20)
    pass
    