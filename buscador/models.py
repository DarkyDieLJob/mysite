from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    Barras = models.IntegerField()
    Codigo = models.CharField(max_length=20)
    Relacional = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=200)
    Precio = models.CharField(max_length=20)
    Porcentaje = models.CharField(max_length=4)
    Pack = models.CharField(max_length=20)
    Final = models.CharField(max_length=20)
    Trabajado = models.CharField(max_length=20)
    Actualizado = models.CharField(max_length=20)
    Fecha = models.CharField(max_length=20)
    Stock = models.CharField(max_length=20)
    Probeedores = models.CharField(max_length=20)
    Cantidad = models.CharField(max_length=20)
    Imagen = models.CharField(max_length=20)
    #Agregado = models.DateField(auto_now_add=True, blank=True, null=True)
    #Editado = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        text = "{}----- ${}".format(self.Nombre,self.Precio)
        return text