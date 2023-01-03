from django.db import models
from datetime import datetime

# Create your models here.
class Registro_General(models.Model):


	pass

class Factura_Proveedor(models.Model):

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

	FACTURA = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
	)

	proveedor = models.CharField(max_length=5, choices=PROVEEDORES, default=Amaya)
	numero_factura = models.IntegerField(default=0000000000)
	tipo_de_factura = models.CharField(max_length=1, choices=FACTURA, default='A')
	numero_del_tipo = models.IntegerField(default=00000)
	fecha = models.DateField(auto_now_add=False, blank=False)
	pass

class Factura_Blanco(models.Model):
	factura_proveedor = models.OneToOneField(Factura_Proveedor, on_delete=models.CASCADE)
	subtotal_1 = models.FloatField(default=0.0)
	subtotal_2 = models.FloatField(default=0.0)
	iva_21 = models.FloatField(default=0.0)
	iva_10_5 = models.FloatField(default=0.0)
	total_1 = models.FloatField(default=0.0)
	total_2 = models.FloatField(default=0.0)
	total_final = models.FloatField(default=0.0)
	pass	

class Factura_Negro(models.Model):
	factura_proveedor = models.OneToOneField(Factura_Proveedor, on_delete=models.CASCADE)
	subtotal_1 = models.FloatField(default=0.0)
	subtotal_2 = models.FloatField(default=0.0)
	iva_21 = models.FloatField(default=0.0)
	iva_10_5 = models.FloatField(default=0.0)
	total_1 = models.FloatField(default=0.0)
	total_2 = models.FloatField(default=0.0)
	total_final = models.FloatField(default=0.0)
	pass