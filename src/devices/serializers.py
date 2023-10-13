from .models import Devices, Producers, House, Address,  City, TempResults, HumidityResults
from rest_framework.serializers import ModelSerializer



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


class TempSerializer(ModelSerializer):
    device = DeviceSerializer

    class Meta:
        model = TempResults
        fields = ['id', 'device', 'created', 'temp_value', 'heat_index']


class HumiSerializer(ModelSerializer):
    device = DeviceSerializer

    class Meta:
        model = HumidityResults
        fields = ['id', 'device', 'created', 'humidity', 'absolute_humidity']
