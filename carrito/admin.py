from django.contrib import admin
from .models import Carrito

# Register your models here.
@admin.register(Carrito)
class PersonAdmin(admin.ModelAdmin):
    pass