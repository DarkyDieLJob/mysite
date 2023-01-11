# Generated by Django 4.1.3 on 2023-01-11 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Cantidad',
        ),
        migrations.AlterField(
            model_name='item',
            name='Final',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='item',
            name='Porcentaje',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='item',
            name='Precio',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='item',
            name='Stock',
            field=models.FloatField(default=0.0),
        ),
    ]
