from django.urls import path
from .views import DeviceListActive, Results

app_name = 'device'

urlpatterns = [
    path("list/", DeviceListActive.as_view(), name="device-list-active"),
    path("<int:id>/results/<str:type_of>/", Results.as_view(), name="device-results")
]
