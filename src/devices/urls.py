from django.urls import path
from .views import DeviceListActive

app_name = 'device'

urlpatterns = [
    path("list/", DeviceListActive.as_view(), name="device-list-active")
]
