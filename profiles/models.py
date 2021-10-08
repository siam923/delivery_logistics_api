from django.db import models
from django.conf import settings
from area.models import Hub


class DeliveryMan(models.Model):
    BRONZE = 'B'
    SILVER = 'S'
    GOLD = 'G'
    PICKUP = 'P'
    DELIVERY = 'D'
    BOTH = 'A'
    CHOICES = [
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
    ]
    WORKCHOICE = [
        (PICKUP, 'Pickup'),
        (DELIVERY, 'Delivery'),
        (BOTH, 'Both'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='worker', on_delete=models.CASCADE)
    membership = models.CharField(
        max_length=1, choices=CHOICES, default=BRONZE)
    work_type = models.CharField(
        max_length=1, choices=WORKCHOICE, default=PICKUP)
    nid = models.CharField(max_length=30)
    points = models.DecimalField(max_digits=6, decimal_places=2)
    registration_date = models.DateTimeField(auto_now=True)
    nid_front = models.URLField(null=True, blank=True, max_length=200)
    nid_back = models.URLField(null=True, blank=True, max_length=200)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.first_name)


class WorkerHub(models.Model):
    worker = models.ForeignKey(DeliveryMan, on_delete=models.CASCADE)
    hub = models.ForeignKey(Hub, related_name='workers',
                            on_delete=models.CASCADE)


class Merchant(models.Model):
    BRONZE = 'B'
    SILVER = 'S'
    GOLD = 'G'
    CHOICES = [
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='merchant', on_delete=models.CASCADE)
    membership = models.CharField(
        max_length=1, choices=CHOICES, default=BRONZE)
    nid = models.CharField(max_length=30)
    nid_front = models.URLField(null=True, blank=True, max_length=200)
    nid_back = models.URLField(null=True, blank=True, max_length=200)
    points = models.DecimalField(max_digits=6, decimal_places=2)
    registration_date = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.first_name)
