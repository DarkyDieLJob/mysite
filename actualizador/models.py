from django.db import models
from datetime import datetime

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

    Amaya = '/A'
    Bauen = '/B'
    Cedica = '/C'
    Crimaral = '/Cr'
    Danirox = '/Dx'
    Dist3D = '/3D'
    CityBell = '/Cb'
    Econo = '/E'
    EQ = '/Eq'
    FerriPlast = '/Fp'
    Fischer = '/F'
    Maglia = '/M'
    Parsecs = '/P'
    Sibon = '/Sn'
    Sumar = '/S'
    Violini = '/V'
    YAYI = '/Y'

    PROVEEDORES = (
        (Amaya, 'Amaya'),
        (Bauen, 'Bauen'),
        (Cedica, 'Cedica'),
        (Crimaral, 'Crimaral'),
        (Danirox, 'Danirox'),
        (Dist3D, 'Dist3D'),
        (CityBell, 'CityBell'),
        (Econo, 'Econo'),
        (EQ, 'EQ'),
        (FerriPlast, 'FerriPlast'),
        (Fischer, 'Fischer'),
        (Maglia, 'Maglia'),
        (Parsecs, 'Parsecs'),
        (Sibon, 'Sibon'),
        (Sumar, 'Sumar'),
        (Violini, 'Violini'),
        (YAYI, 'YAYI'),
    )
    
    nombre = models.CharField(
        max_length=4,
        choices=PROVEEDORES,
        default=Amaya,
    )
    
    agregado = models.DateField(auto_now_add=True, blank=True)
    editado = models.DateField(auto_now=True, blank=True)
    archivo = models.FileField(upload_to="", null=True, blank=True)
    
    def __str__(self):
        return self.nombre

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

