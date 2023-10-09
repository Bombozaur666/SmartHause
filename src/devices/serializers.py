from .models import Devices, Producers, House, Address, Room, City
from rest_framework.serializers import ModelSerializer


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name'
        ]


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
    rooms = RoomSerializer()
    address = AddressSerializer()

    class Meta:
        model = House
        fields = [
            'id',
            'name',
            'rooms',
            'address'
        ]


class ProducersSerializer(ModelSerializer):
    class Meta:
        model = Producers
        fields = [
            'id',
            'name',
            'active',
            'website',
            'comment'
        ]


class DeviceSerializer(ModelSerializer):
    house = HouseSerializer()
    producer = ProducersSerializer()

    class Meta:
        model = Devices
        fields = [
            'id',
            'name',
            'producer',
            'api_url',
            'type',
            'house',
            'active',
            'ip_address',
            'port',
            'protocol'
        ]
