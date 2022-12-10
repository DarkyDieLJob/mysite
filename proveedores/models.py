from django.db import models

# Create your models here.
class Lista_Pedidos(models.Model):
    Proveedor = models.CharField(max_length=20)
    Codigo_lista = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=20)
    Cantidad = models.CharField(max_length=20)
    pass