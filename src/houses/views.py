from rest_framework.response import Response
from .models import House
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import DeviceSerializer, TempSerializer, HumiSerializer
from .models import TempResults, HumidityResults


# Create your views here.

class HouseListActive(generics.ListAPIView):
    model = House
    serializer_class = DeviceSerializer
    queryset = House.objects.filter(active=True)


class RemoveHouse(generics.GenericAPIView):
    def delete(self, request, pk):
        print(f'pk: {pk}')
        device = get_object_or_404(House, id=pk)
        print(f'device: {device}')
        device.delete()
        return Response(status=status.HTTP_200_OK)
