from __future__ import absolute_import, unicode_literals
from celery import shared_task
from devices.models import Devices
from results.models import HumidityResults, TempResults
from datetime import datetime
from httpx import AsyncClient, TimeoutException
from asgiref.sync import async_to_sync


async def async_temp_and_humidity():
    bulk_temperature = []
    bulk_humidity = []
    content = []
    time_now = datetime.now()
    devices = Devices.objects.filter(active=True,
                                     type=Devices.THERMAL_AND_HUMIDITY)
    async with AsyncClient() as client:
        async for device in devices:
            try:
                response = await client.get(f'{device.protocol}://{device.ip_address}:{device.port}/state',
                                            timeout=1)
                result = response.json()
                content.append(result)
                temp = TempResults(device=device,
                                   created=time_now,
                                   temp_value=(result['multiSensor']['sensors'][1]['value']/100),
                                   heat_index=(result['multiSensor']['sensors'][4]['value']/100),
                                   )
                hum = HumidityResults(device=device,
                                      created=time_now,
                                      humidity=(result['multiSensor']['sensors'][0]['value']/100),
                                      absolute_humidity=(result['multiSensor']['sensors'][2]['value']/100))

                bulk_temperature.append(temp)
                bulk_humidity.append(hum)
            except TimeoutException:
                pass

    await TempResults.objects.abulk_create(bulk_temperature)
    await HumidityResults.objects.abulk_create(bulk_humidity)

    return content


@shared_task(serializer='json', name="temp_and_humidity_task")
def temp_and_humidity(*args, **kwargs):
    context = async_to_sync(async_temp_and_humidity)()
    return context
