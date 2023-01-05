from django.contrib import admin
from .models import Condicionales, Proveedores

# Register your models here.
@admin.register(Condicionales)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Proveedores)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['nombre','agregado','editado']
    search_fields = ['nombre',]
    pass