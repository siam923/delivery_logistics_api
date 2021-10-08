from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Merchant, DeliveryMan, WorkerHub
from .serializers import MerchantSerializer, DeliveryManSerializer, WorkerHubSerializer


class MerchantList(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class MerchantDetail(generics.RetrieveUpdateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class WorkertList(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class WorkerDetail(generics.RetrieveUpdateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class WorkerHubDetail(generics.RetrieveUpdateAPIView):
    queryset = WorkerHub.objects.all()
    serializer_class = WorkerHubSerializer
