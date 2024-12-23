# Generated by Django 5.1.3 on 2024-12-05 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeDispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'TipoDeDispositivo',
                'verbose_name_plural': 'TipoDeDispositivos',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_adress', models.CharField(max_length=17, unique=True, verbose_name='MAC Address')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre del dispositivo')),
                ('estado', models.CharField(max_length=1, verbose_name='Estado')),
                ('fecha_fabricacion', models.DateField(verbose_name='Fecha de Fabricacion')),
                ('fecha_registro', models.DateTimeField(auto_now=True, verbose_name='Fecha de registro')),
                ('criticidad_energetica', models.IntegerField(verbose_name='Criticidad Energetica')),
                ('consumo_energia', models.FloatField(verbose_name='Consumo de energia')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivo.tipodedispositivo')),
            ],
            options={
                'verbose_name': 'Dispositivo',
                'verbose_name_plural': 'Dispositivos',
            },
        ),
    ]
