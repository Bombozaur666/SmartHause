from django.contrib import admin
from .models import Devices, TempResults, HumidityResults

admin.site.register(Devices)
admin.site.register(TempResults)
admin.site.register(HumidityResults)
