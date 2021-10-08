from django.db.models.signals import post_save
from django.dispatch import receiver
from parcels.models import ParcelOrder, Delivery
from area.models import Area, Hub


@receiver(post_save, sender=ParcelOrder)
def create_delivery_for_new_order(sender, **kwargs):
    if kwargs['created']:
        parcel_area = kwargs['instance'].customer_area.id
        # hub_id = Hub.objects.get(area=parcel_area)
        hub_instance = Hub.objects.get(area=parcel_area)
        Delivery.objects.create(
            parcel=kwargs['instance'], destination_hub=hub_instance)
