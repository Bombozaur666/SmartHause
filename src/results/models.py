from django.db import models
from devices.models import Devices
# Create your models here.


class TempResults(models.Model):
    device = models.ForeignKey(Devices,
                               on_delete=models.DO_NOTHING)

    created = models.DateTimeField()

    temp_value = models.IntegerField()

    heat_index = models.IntegerField(null=True,
                                     blank=True)


class HumidityResults(models.Model):
    device = models.ForeignKey(Devices,
                               on_delete=models.DO_NOTHING)

    created = models.DateTimeField()

    humidity = models.IntegerField()
    absolute_humidity = models.IntegerField()
