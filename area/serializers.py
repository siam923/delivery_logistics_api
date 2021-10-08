from rest_framework import serializers
from .models import DeliveryCharge, District, Zone, Area, Hub


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']


class DeliveryChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCharge
        fields = ['id', 'cost', 'description']


class ZoneSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    charge = DeliveryChargeSerializer()

    class Meta:
        model = Zone
        fields = ['id', 'name', 'charge', 'district']


class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = ['id', 'name', 'address']


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ['id', 'name', 'hub', 'zone']


class AreaDetailSerializer(serializers.ModelSerializer):
    hub = HubSerializer()
    zone = ZoneSerializer()

    class Meta:
        model = Area
        fields = ['id', 'name', 'hub', 'zone']
