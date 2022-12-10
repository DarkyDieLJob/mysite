from django.contrib import admin
from .models import Planilla_Diaria , Resumen_Diario

# Register your models here.
@admin.register(Planilla_Diaria)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Resumen_Diario)
class PersonAdmin(admin.ModelAdmin):
    pass
