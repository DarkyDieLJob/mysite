# Generated by Django 4.1.3 on 2022-12-25 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actualizador', '0002_delete_prueva_rename_condicion_proveedores_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedores',
            name='dolar',
        ),
    ]