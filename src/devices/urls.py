from django.urls import path
from .views import DeviceListActive, Results, RemoveDevice

app_name = 'device'

urlpatterns = [
    path("list/", DeviceListActive.as_view(), name="device-list-active"),
    path("<int:pk>/results/", Results.as_view(), name="device-results"),
    path("<int:pk>/remove/", RemoveDevice.as_view(), name="device-remove")
]
