from django.db import models

# Create your models here.
'''
class Condicionales(models.Model):
    proveedor = models.CharField(max_length=20,primary_key=True)
    codigo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=1)
    precio = models.CharField(max_length=1)
    dolar = models.FloatField(max_length=29)
    porcentaje = models.FloatField()
    inicio = models.CharField(max_length=2)
    extension = models.CharField(max_length=20)
    pass

class Proveedores(models.Model):
    proveedor = models.CharField(max_length=20)
    condicion = models.CharField(max_length=20)
    dolar = models.FloatField(max_length=29)
    fecha = models.CharField(max_length=20)
    pass

class Planilla(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    moneda = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=20)
    pass

class Revision(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    moneda = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=20)
    pass

class Sin_Codigo(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    moneda = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=20)
    pass'''

class Prueva(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    moneda = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=20)
    pass