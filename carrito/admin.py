from django.contrib import admin
from .models import Items_Carrito, Carrito

# Register your models here.
@admin.register(Carrito)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Items_Carrito)
class PersonAdmin(admin.ModelAdmin):
    pass