from django.db import models
from devices.models import Devices
# Create your models here.


class BaseResult(models.Model):
    device = models.ForeignKey(Devices,
                               on_delete=models.DO_NOTHING)

    created = models.DateTimeField()

    class Meta:
        abstract = True


class TempResults(BaseResult):
    temp_value = models.IntegerField()

    heat_index = models.IntegerField(null=True,
                                     blank=True)

    def __str__(self):
        return f"{self.device.name} at {self.created}"


class HumidityResults(BaseResult):
    humidity = models.IntegerField()
    absolute_humidity = models.IntegerField()

    def __str__(self):
        return f"{self.device.name} at {self.created}"
