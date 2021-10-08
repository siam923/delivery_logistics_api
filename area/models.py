from django.db import models
from django.core.validators import MinValueValidator

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DeliveryCharge(models.Model):
    cost = models.PositiveIntegerField(
        validators=[MinValueValidator(10)])
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description
    

class Zone(models.Model):
    name = models.CharField(max_length=100)
    charge = models.ForeignKey(DeliveryCharge, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.charge.cost}'

class Hub(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100) # address of hub
    
    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=30)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.zone.name} -> {self.name}'

