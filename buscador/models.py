from django.db import models
from datetime import datetime

# Create your models here.
class Item(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    Barras = models.IntegerField(default=0)
    Codigo = models.CharField(max_length=20)
    Relacional = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=200)
    Precio = models.FloatField(default=0.0)
    Porcentaje = models.FloatField(default=0.0)
    Pack = models.FloatField(default=0.0)
    Final = models.FloatField(default=0.0)
    Trabajado = models.BooleanField(default=False)
    Actualizado = models.BooleanField(default=False)
    Fecha = models.DateField(auto_now_add=True, blank=True)
    Stock = models.FloatField(default=0.0)
    Probeedores = models.CharField(max_length=20)
    Imagen = models.CharField(max_length=20)

    def __str__(self):
        text = "{}----- ${}".format(self.Nombre,self.Precio)
        return text