from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Carrito(models.Model):
    usuario = models.IntegerField()
    pass 

class Items_Carrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.FloatField(default=0.0)
    cantidad = models.FloatField(default=0.0)
    pass 

class Finalizar_Venta(models.Model):
    nombre = models.CharField(max_length=20) #nombre de la entrada
    fecha = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)
    total = models.FloatField(default=0.0)
    metodo_pago = models.CharField(max_length=20)
    cuotas = models.IntegerField(default=1)
    estado = models.CharField(max_length=20)
    pass 