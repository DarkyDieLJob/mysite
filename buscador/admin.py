from django.contrib import admin
from .models import Item

@admin.register(Item)
class PersonAdmin(admin.ModelAdmin):
    pass