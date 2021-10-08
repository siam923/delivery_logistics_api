from django.contrib import admin
from . import models


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'store_code', 'owner']


@admin.register(models.PickupAddress)
class PickupAddressAdmin(admin.ModelAdmin):
    list_display = ['name', 'store']


@admin.register(models.ParcelOrder)
class PercelOrderAdmin(admin.ModelAdmin):
    list_display = ['parcel_id', 'creationDate', 'customer_phone']


@admin.register(models.OrderCost)
class OrderCostAdmin(admin.ModelAdmin):
    list_display = ['orderid', 'fee']

    @admin.display()
    def orderid(self, cost):
        return cost.order.parcel_id

    @admin.display()
    def fee(self, cost):
        return cost.total


@admin.register(models.Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['orderid', 'pickup_status', 'delivery_status']

    @admin.display()
    def orderid(self, delivery):
        return delivery.parcel.parcel_id


@admin.register(models.ParcelIssue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['orderid', 'last_update', 'issue_status']

    @admin.display()
    def orderid(self, issue):
        return issue.issue_for.parcel_id


@admin.register(models.AccountReceivable)
class AccountReceivableAdmin(admin.ModelAdmin):
    list_display = ['merchant_name', 'due_amount']

    @admin.display()
    def merchant_name(self, acc):
        return acc.merchant.user.first_name


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['merchant_name', 'processed']

    @admin.display()
    def merchant_name(self, obj):
        return obj.merchant.user.first_name


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['merchant_name', 'date']

    @admin.display()
    def merchant_name(self, obj):
        return obj.payment_to.user.first_name


admin.site.register(models.CustomerInfo)
admin.site.register(models.DeliveryType)
admin.site.register(models.ItemType)
