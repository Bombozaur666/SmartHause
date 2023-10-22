from rest_framework.response import Response
from .models import Devices
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import DeviceSerializer, TempSerializer, HumiSerializer
from .models import TempResults, HumidityResults


# Create your views here.

class DeviceListActive(generics.ListAPIView):
    model = Devices
    serializer_class = DeviceSerializer
    queryset = Devices.objects.filter(active=True)


class Results(generics.GenericAPIView):
    def get(self, request, pk):
        device = get_object_or_404(Devices, id=pk)
        if device.active:
            results_humidity = get_list_or_404(HumidityResults, device__pk=device.pk)
            results_temperature = get_list_or_404(TempResults, device__pk=device.pk)
            serializer_humidity = HumiSerializer(results_humidity, many=True)
            serializer_temperature = TempSerializer(results_temperature, many=True)
            return Response(
                {'temperature': serializer_temperature.data,
                 'humidity': serializer_humidity.data},
                status=status.HTTP_200_OK)
        else:
            return Response(status.HTTP_403_FORBIDDEN)


class RemoveDevice(generics.GenericAPIView):
    def delete(self, request, pk):
        device = get_object_or_404(Devices, id=pk)
        device.delete()
        return Response(status=status.HTTP_200_OK)