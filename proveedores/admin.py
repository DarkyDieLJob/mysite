from django.contrib import admin
from .models import Lista_Pedidos

# Register your models here.
@admin.register(Lista_Pedidos)
class PersonAdmin(admin.ModelAdmin):
    pass
