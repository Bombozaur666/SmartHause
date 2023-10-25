from django.contrib import admin
from .models import Devices, Producers, TempResults, HumidityResults

admin.site.register(Devices)
admin.site.register(Producers)
admin.site.register(TempResults)
admin.site.register(HumidityResults)
