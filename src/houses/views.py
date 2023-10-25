from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import HouseSerializer
from .models import House


# Create your views here.

class HouseListActive(generics.ListAPIView):
    model = House
    serializer_class = HouseSerializer
    queryset = House.objects.all()


class RemoveHouse(generics.GenericAPIView):
    def delete(self, request, pk):
        house = get_object_or_404(House, id=pk)
        house.delete()
        return Response(status=status.HTTP_200_OK)
