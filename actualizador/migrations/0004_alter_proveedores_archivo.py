# Generated by Django 4.1.3 on 2023-01-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualizador', '0003_remove_proveedores_dolar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
