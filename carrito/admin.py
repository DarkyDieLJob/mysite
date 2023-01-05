from django.contrib import admin
from .models import Carrito_Items, Carrito

# Register your models here.
@admin.register(Carrito)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Carrito_Items)
class PersonAdmin(admin.ModelAdmin):
    pass