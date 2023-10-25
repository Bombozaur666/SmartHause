from django.urls import path
from .views import HouseListActive, RemoveHouse

app_name = 'house'

urlpatterns = [
    path("list/", HouseListActive.as_view(), name="house-list-active"),
    path("<int:pk>/remove/", RemoveHouse.as_view(), name="house-remove")
]
