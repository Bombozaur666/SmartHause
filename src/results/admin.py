from django.contrib import admin
from .models import TempResults, HumidityResults

# Register your models here.

admin.site.register(TempResults)
admin.site.register(HumidityResults)
