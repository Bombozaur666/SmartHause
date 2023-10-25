from django.urls import path
from .views import HouseListActive, RemoveHouse

app_name = 'device'

urlpatterns = [
    path("list/", HouseListActive.as_view(), name="device-list-active"),
    path("<int:pk>/remove/", RemoveHouse.as_view(), name="device-remove")
]
