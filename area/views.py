from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators import permission_classes, action
# from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from .models import District, DeliveryCharge, Zone, Hub, Area
from .serializers import DistrictSerializer, DeliveryChargeSerializer, ZoneSerializer, HubSerializer, AreaSerializer


class DistrictListView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DeliveryChargeListView(generics.ListAPIView):
    queryset = DeliveryCharge.objects.all()
    serializer_class = DeliveryCharge
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact', ],
    }

class ZoneListView(generics.ListAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'district__id': ['exact', ],
    }


class AreaListView(generics.ListAPIView):
    serializer_class = AreaSerializer

    def get_queryset(self):
        return Area.objects.filter(zone=self.kwargs['pk'])
    
