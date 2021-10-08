from django.contrib import admin
from . import models


admin.site.register(models.District)
admin.site.register(models.DeliveryCharge)
admin.site.register(models.Hub)
admin.site.register(models.Zone)
admin.site.register(models.Area)