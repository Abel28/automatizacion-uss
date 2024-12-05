from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _ 

class TipoDeDispositivo(models.Model):

    descripcion = models.CharField("Descripcion", max_length=50, null=False)

    class Meta:
        verbose_name = _("TipoDeDispositivo")
        verbose_name_plural = _("TipoDeDispositivos")

    def __str__(self):
        return self.descripcion

    def get_absolute_url(self):
        return reverse("TipoDeDispositivo_detail", kwargs={"pk": self.pk})
    

ESTADO_CHOICES = [
    ('E', 'Encendido'),
    ('A', 'Apagado'),
]

CRITICIDAD_CHOICES = [
    (1, 'Bajo'),
    (2, 'Medio'),
    (3, 'Alto')
]


class Dispositivo(models.Model):

    mac_adress = models.CharField("MAC Address", max_length=17, unique=True, null=False)
    nombre = models.CharField("Nombre del dispositivo", max_length=50, unique=True)
    estado = models.CharField("Estado", max_length=1, null=False, choices=ESTADO_CHOICES)
    fecha_fabricacion = models.DateField("Fecha de Fabricacion", null=False)
    fecha_registro = models.DateTimeField("Fecha de registro", auto_now=True)
    criticidad_energetica = models.IntegerField("Criticidad Energetica", null=False, choices=CRITICIDAD_CHOICES)
    consumo_energia = models.FloatField("Consumo de energia", null=False)
    tipo = models.ForeignKey(TipoDeDispositivo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Dispositivo")
        verbose_name_plural = _("Dispositivos")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Dispositivo_detail", kwargs={"pk": self.pk})
