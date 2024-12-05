# Generated by Django 5.1.3 on 2024-12-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='criticidad_energetica',
            field=models.IntegerField(choices=[(1, 'Bajo'), (2, 'Medio'), (3, 'Alto')], verbose_name='Criticidad Energetica'),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='estado',
            field=models.CharField(choices=[('E', 'Encendido'), ('A', 'Apagado')], max_length=1, verbose_name='Estado'),
        ),
    ]
