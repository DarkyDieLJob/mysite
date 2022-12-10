from django.contrib import admin
from .models import Planilla_Diaria , Resumen_Diario, Resumen_Mensual

# Register your models here.
@admin.register(Planilla_Diaria)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Resumen_Diario)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Resumen_Mensual)
class PersonAdmin(admin.ModelAdmin):
    pass
