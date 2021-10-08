from rest_framework import serializers
from profiles.serializers import MerchantSerializer
from profiles.serializers import SimpleMerchantSerializer
from .models import Store, PickupAddress, DeliveryType, CustomerInfo, ItemType, ParcelOrder, OrderCost, Delivery, ParcelIssue, AccountReceivable, Payment, Invoice


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'phone', 'website',
                  'facebook', 'address', 'owner']


class PickupAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupAddress
        fields = ['id', 'name', 'store', 'area', 'address']


class CustomerInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = ['phone_no', 'name', 'customer_orders']


class CustomerInfoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = ['phone_no']


class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = ['id', 'delivery_type']


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ['id', 'item_type']


class ParcelOrderSerializer(serializers.ModelSerializer):
    customer_phone = serializers.CharField()

    class Meta:
        model = ParcelOrder
        fields = ['id', 'parcel_id', 'delivery_type', 'creationDate', 'receiver_name', 'customer_phone', 'store', 'pickup_address',
                  'collection_amount', 'customer_area', 'customer_address', 'item_type', 'item_description', 'item_weight', 'instruction']
        read_only_fields = ('creationDate',)

    def create(self, validated_data):
        phone_no = validated_data.pop('customer_phone').strip()
        customer_obj, created = CustomerInfo.objects.get_or_create(
            phone_no=phone_no)
        return ParcelOrder.objects.create(customer_phone=customer_obj, **validated_data)


class OrderCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCost
        fields = ['id', 'delivery_charge', 'cod_fee', 'discounts',
                  'additional_charge', 'total', 'order']


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'parcel', 'pickupman', 'pickup_status', 'delivery_status',
                  'current_hub', 'destination_hub', 'deliveryman', 'last_update']


class ParcelIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelIssue
        fields = ['id', 'last_update', 'issue_status', 'issue_for',
                  'issue_description', 'issue_response']


class AccountReceivableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountReceivable
        fields = ['id', 'due_amount', 'merchant']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'pending', 'delivery_due',
                  'inprocess', 'processed', 'merchant']


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'payment_to', 'data', 'amount']
