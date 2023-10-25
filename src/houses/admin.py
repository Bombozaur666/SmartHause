from django.contrib import admin

from .models import Address, City, House

# Register your models here.
admin.site.register(Address)
admin.site.register(City)
admin.site.register(House)
