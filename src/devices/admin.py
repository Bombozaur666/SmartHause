from django.contrib import admin
from .models import Devices, House, Producers, Address, City, TempResults, HumidityResults

admin.site.register(Devices)

admin.site.register(Producers)

admin.site.register(TempResults)
admin.site.register(HumidityResults)
