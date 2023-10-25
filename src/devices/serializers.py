from .models import Devices, Producers, TempResults, HumidityResults
from rest_framework.serializers import ModelSerializer
from ..houses.serializers import HouseSerializer


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
