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
    def get(self, request, id, type_of):
        device = get_object_or_404(Devices, id=id)
        if type_of == Devices.THERMAL:
            results = get_list_or_404(TempResults, device__id=id)
            serializer = TempSerializer(results)
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        elif type_of == Devices.HUMIDITY:
            results = get_list_or_404(HumidityResults, device__id=id)
            serializer = HumiSerializer(results)
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
