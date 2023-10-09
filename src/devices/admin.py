from django.contrib import admin
from .models import Devices, House, Producers, Address, City

admin.site.register(Devices)
admin.site.register(House)
admin.site.register(Producers)
admin.site.register(Address)
admin.site.register(City)
