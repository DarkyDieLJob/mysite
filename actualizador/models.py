from django.db import models

# Create your models here.

class Condicionales(models.Model):
    proveedor = models.CharField(max_length=20,primary_key=True)
    col_codigo = models.CharField(max_length=1)
    col_nombre = models.CharField(max_length=1)
    col_precio = models.CharField(max_length=1)
    dolar = models.FloatField(max_length=29, default=0.0)
    porcentaje = models.FloatField()
    inicio = models.CharField(max_length=2)
    extension = models.CharField(max_length=20)
    pass

class Proveedores(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.CharField(max_length=12)
    
    #que columna tiene el dato dolar
    dolar = models.FloatField(max_length=1)
    
    #que condicion para detectar el dato
    archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
    
    pass

class Planilla(models.Model):
    proveedor = models.CharField(max_length=20)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    moneda = models.CharField(max_length=20)
    
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
    condicion_moneda = models.CharField(max_length=20, default='')
    proveedor = models.CharField(max_length=20)
    pass

