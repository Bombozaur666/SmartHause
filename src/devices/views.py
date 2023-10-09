from .models import Devices
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import DeviceSerializer


# Create your views here.

class DeviceListActive(generics.ListAPIView):
    model = Devices
    serializer_class = DeviceSerializer
    queryset = Devices.objects.filter(active=True)
