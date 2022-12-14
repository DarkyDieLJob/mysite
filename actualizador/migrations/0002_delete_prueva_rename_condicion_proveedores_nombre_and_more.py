# Generated by Django 4.1.3 on 2022-12-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualizador', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prueva',
        ),
        migrations.RenameField(
            model_name='proveedores',
            old_name='condicion',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='proveedores',
            name='proveedor',
        ),
        migrations.AddField(
            model_name='proveedores',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='archivos/'),
        ),
        migrations.AddField(
            model_name='sin_codigo',
            name='condicion_moneda',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='dolar',
            field=models.FloatField(max_length=1),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='fecha',
            field=models.CharField(max_length=12),
        ),
    ]
