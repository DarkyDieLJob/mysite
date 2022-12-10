from django.db import models

# Create your models here.
class Planilla_Diaria(models.Model):
    Fecha = models.CharField(max_length=20)
    Hora = models.CharField(max_length=20)
    Efectivo = models.CharField(max_length=20)
    Cant_efectivo = models.CharField(max_length=20)
    Visa_credito = models.CharField(max_length=20)
    Cant_visa_credito = models.CharField(max_length=20)
    Master_credito = models.CharField(max_length=20)
    Cant_master_credito = models.CharField(max_length=20)
    Visa_debito = models.CharField(max_length=20)
    Cant_visa_debito = models.CharField(max_length=20)
    Maestro = models.CharField(max_length=20)
    Cant_maestro = models.CharField(max_length=20)
    Caja_inicial = models.CharField(max_length=20)
    Caja_final = models.CharField(max_length=20)
    pass

class Resumen_Diario(models.Model):
    Fecha = models.CharField(max_length=20)
    Blanco = models.CharField(max_length=20)
    Negro = models.CharField(max_length=20)
    Diferencia = models.CharField(max_length=20)
    Total_diario = models.CharField(max_length=20)
    Credito = models.CharField(max_length=20)
    Debito = models.CharField(max_length=20)
    Mercado_pago = models.CharField(max_length=20)
    Venta_online = models.CharField(max_length=20)
    pass 

class Resumen_Mensual(models.Model):
    Fecha = models.CharField(max_length=20)
    