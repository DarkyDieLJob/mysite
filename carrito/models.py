from django.db import models

# Create your models here.

class Carrito(models.Model):
    usuario = models.CharField(max_length=20)
    pass 

class Items_Carrito(models.Model):
    carrito = models.ManyToManyField(Carrito, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20)
    pass 

class Finalizar_Venta(models.Model):
    nombre = models.CharField(max_length=20) #nombre de la entrada
    fecha = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)
    total = models.CharField(max_length=20)
    metodo_pago = models.CharField(max_length=20)
    cuotas = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    pass 