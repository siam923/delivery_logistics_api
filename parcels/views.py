from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import permission_classes, action
# from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from .models import Store, PickupAddress, CustomerInfo, DeliveryType, ItemType, ParcelOrder, OrderCost, Payment, Invoice, Delivery, AccountReceivable
from .serializers import (StoreSerializer, PickupAddressSerializer, CustomerInfoSimpleSerializer,
                          CustomerInfoDetailSerializer, DeliveryTypeSerializer, ItemTypeSerializer, ParcelOrderSerializer,
                          OrderCostSerializer, PaymentSerializer, InvoiceSerializer, DeliverySerializer,
                          AccountReceivableSerializer)


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class MerchantStoreList(generics.ListCreateAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        return Store.objects.filter(owner=self.kwargs['pk'])


class PickupAddressList(generics.ListCreateAPIView):
    serializer_class = PickupAddressSerializer

    def get_queryset(self):
        # pk->store_id
        return PickupAddress.objects.filter(store=self.kwargs['pk'])


class PickupAddressDetail(generics.ListCreateAPIView):
    serializer_class = PickupAddressSerializer

    def get_queryset(self):
        # pk->store_id
        return PickupAddress.objects.filter(store=self.kwargs['pk'])


class CustomerList(generics.ListCreateAPIView):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerInfoSimpleSerializer


class DeliveryTypeList(generics.ListCreateAPIView):
    queryset = DeliveryType.objects.all()
    serializer_class = DeliveryTypeSerializer


class ItemTypeList(generics.ListCreateAPIView):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer


class ParcelOrdersAll(generics.ListCreateAPIView):
    queryset = ParcelOrder.objects.all()
    serializer_class = ParcelOrderSerializer
    filterfilter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact', ],
        'parcel_id': ['iexact', ],
        'creationDate': ['gte', 'lte', 'exact', 'gt', 'lt'],
        'customer_phone': ['iexact'],
    }


class OrderCostList(generics.ListCreateAPIView):
    serializer_class = OrderCostSerializer

    def get_queryset(self):
        return OrderCost.objects.filter(order=self.kwargs['pk'])


class DeliveryList(generics.ListAPIView):
    serializer_class = DeliverySerializer
    filterfilter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact', ],
        'parcel': ['iexact', ],
        'pickupman': ['exact'],
        'destination_hub': ['exact'],
        'current_hub': ['exact'],
        'deliveryman': ['exact'],
        'pickup_status': ['iexact'],
        'delivery_status': ['iexact']
    }

    def get_queryset(self):
        return Delivery.objects.filter(parcel=self.kwargs['pk'])


class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        return Delivery.objects.filter(parcel=self.kwargs['parcel_id'], id=self.kwargs['pk'])


# Delivery List by order__pickupaddress__hub
