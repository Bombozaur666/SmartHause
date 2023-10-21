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
    def get(self, request, id):
        device = get_object_or_404(Devices, id=id)
        if device.active == True:
            results_humidity = get_list_or_404(HumidityResults, device__id=id)
            results_temp = get_list_or_404(TempResults, device__id=id)
            serializer_humidity = HumiSerializer(results_humidity)
            serializer_temp = TempSerializer(results_temp)
            return Response(
                {'temp': serializer_temp.data,
                 'humidity': serializer_humidity.data},
                status=status.HTTP_200_OK)
        else:
            return Response(status.HTTP_403_FORBIDDEN)
