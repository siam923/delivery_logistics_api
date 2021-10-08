from rest_framework import serializers
from core.serializers import SimpleUserSerializer
from core.serializers import SimpleUserSerializer
from .models import Merchant, DeliveryMan, WorkerHub


class SimpleMerchantSerializer(serializers.ModelSerializer):
    user_info = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Merchant
        fields = ['id', 'user', 'user_info', 'stores']


class MerchantSerializer(serializers.ModelSerializer):
    user_info = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Merchant
        fields = ['id', 'user', 'user_info', 'membership', 'nid', 'nid_front',
                  'nid_back', 'points', 'registration_date', 'stores']
        read_only_fields = ['registration_date', ]


class DeliveryManSerializer(serializers.ModelSerializer):
    user_info = SimpleUserSerializer(read_only=True)

    class Meta:
        model = DeliveryMan
        fields = ['id', 'user', 'user_info', 'membership', 'nid', 'work_type',
                  'nid_front', 'nid_back', 'points', 'registration_date']
        read_only_fields = ['registration_date', ]


class WorkerHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerHub
        fields = ['id', 'worker', 'hub']
