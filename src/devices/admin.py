from django.contrib import admin
from .models import Devices, Room, House, Producers, Address, City

admin.site.register(Devices)
admin.site.register(Room)
admin.site.register(House)
admin.site.register(Producers)
admin.site.register(Address)
admin.site.register(City)
