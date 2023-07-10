from __future__ import absolute_import, unicode_literals
from celery import shared_task
from devices.models import Devices
from results.models import HumidityResults, TempResults
from datetime import datetime
from httpx import Client, Timeout
from asgiref.sync import async_to_sync


@shared_task(serializer='json', name="temp_and_humidity_task")
def temp_and_humidity(*args, **kwargs):
    bulk_save = []
    time_now = datetime.now()
    devices = Devices.objects.filter(active=True,
                                     type=Devices.THERMAL_AND_HUMIDITY)
    with Client() as client:
        for device in devices:
            response = client.get(f'{device.protocol}://{device.ip_address}:{device.port}/state')
            bulk_save.append(response.content)
    return {'state': bulk_save}
