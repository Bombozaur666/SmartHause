from rest_framework.serializers import ModelSerializer
from .models import City, Address, House


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = [
            'id',
            'name'
        ]


class AddressSerializer(ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Address
        fields = [
            'city',
            'street',
            'zip_code',
            'house_number',
            'flat_number'
        ]


class HouseSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = House
        fields = [
            'id',
            'name',
            'address'
        ]