from __future__ import absolute_import, unicode_literals
from celery import shared_task
from devices.models import Devices
from results.models import HumidityResults, TempResults
from datetime import datetime
from httpx import Client, Timeout
from asgiref.sync import async_to_sync


async def wrapper():
    bulk_save = []
    time_now = datetime.now()
    devices = Devices.objects.filter(active=True,
                                     type=Devices.THERMAL_AND_HUMIDITY)
    timeout = Timeout(1.0)
    async for device in devices:
        with Client() as client:
            response = client.get(f'{device.protocol}://{device.ip_address}:{device.port}/state/extended')
            print(response)
            bulk_save.append(response.json())
    return await bulk_save


@shared_task(serializer='json', name="temp_and_humidity_task")
def temp_and_humidity(*args, **kwargs):
    bulk = async_to_sync(wrapper)()
    return bulk
