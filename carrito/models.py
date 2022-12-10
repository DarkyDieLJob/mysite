from django.db import models

# Create your models here.

class Carrito(models.Model):
    Usuario = models.CharField(max_length=20)
    Codigo = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=20)
    Cantidad = models.CharField(max_length=20)
    Precio = models.CharField(max_length=20)
    pass 

class Finalizar_Venta(models.Model):
    Usuario = models.CharField(max_length=20)
    Fecha = models.CharField(max_length=20)
    Hora = models.CharField(max_length=20)
    Total = models.CharField(max_length=20)
    Metodo_pago = models.CharField(max_length=20)
    Cuotas = models.CharField(max_length=20)
    Estado = models.CharField(max_length=20)
    pass 