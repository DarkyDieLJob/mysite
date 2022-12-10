from django.contrib import admin
from .models import Carrito, Finalizar_Venta

# Register your models here.
@admin.register(Carrito)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Finalizar_Venta)
class PersonAdmin(admin.ModelAdmin):
    pass