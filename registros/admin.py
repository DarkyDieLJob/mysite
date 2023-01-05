from django.contrib import admin
from .models import Factura_Proveedor, Factura_Blanco, Factura_Negro 

# Register your models here.
@admin.register(Factura_Proveedor)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Factura_Blanco)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Factura_Negro)
class PersonAdmin(admin.ModelAdmin):
    pass