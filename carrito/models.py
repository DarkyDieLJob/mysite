from django.db import models

# Create your models here.

class Carrito(models.Model):
    Usuario = models.CharField(max_length=20)
    Codigo = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=20)
    Cantidad = models.CharField(max_length=20)
    Precio = models.CharField(max_length=20)
    pass 