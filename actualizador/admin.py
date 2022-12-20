from django.contrib import admin
from .models import Condicionales

# Register your models here.
@admin.register(Condicionales)
class PersonAdmin(admin.ModelAdmin):
    pass