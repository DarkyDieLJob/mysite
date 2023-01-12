from django.db import models

# Create your models here.

class Carrito(models.Model):
    pass 



class Carrito_Items(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    cantidad = models.FloatField(default=0.0)

    def total_item(self):
        precio = float(self.precio)
        cantidad = self.cantidad
        resultado = precio * cantidad
        print(resultado)
        return resultado

class Finalizar_Venta(models.Model):
    nombre = models.CharField(max_length=20) #nombre de la entrada
    fecha = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)
    total = models.CharField(max_length=20)
    metodo_pago = models.CharField(max_length=20)
    cuotas = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    pass 