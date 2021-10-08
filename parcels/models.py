from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=50)
    store_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    website = models.URLField(max_length=100, null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=50)
    owner = models.ForeignKey(
        "profiles.Merchant", related_name='stores', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name
# class StoreInfo(models.Model):


class PickupAddress(models.Model):
    name = models.CharField(max_length=50)
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE)
    area = models.ForeignKey(
        "area.Area", related_name="pickups", on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class CustomerInfo(models.Model):
    phone_no = models.CharField(
        unique=True, max_length=15, primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True, default='')

    def __str__(self):
        return self.phone_no


class DeliveryType(models.Model):
    delivery_type = models.CharField(max_length=20)

    def __str__(self):
        return self.delivery_type


class ItemType(models.Model):
    item_type = models.CharField(max_length=20)

    def __str__(self):
        return self.item_type


class ParcelOrder(models.Model):
    # Note: Accidental deleting pickup address, store, area wont delete percel orders
    # Track using Filter by parcel id and phone number
    parcel_id = models.CharField(
        max_length=10, blank=True, null=True)  # tracking id
    delivery_type = models.ForeignKey(
        DeliveryType, blank=True, null=True, on_delete=models.SET_NULL)
    creationDate = models.DateTimeField(auto_now=True)
    receiver_name = models.CharField(max_length=50)
    customer_phone = models.ForeignKey(
        CustomerInfo, related_name="customer_orders", on_delete=models.PROTECT)
    store = models.ForeignKey(
        Store, related_name="store_orders", on_delete=models.PROTECT)
    pickup_address = models.ForeignKey(
        PickupAddress, on_delete=models.PROTECT, related_name='parcels')
    collection_amount = models.DecimalField(max_digits=6, decimal_places=2)
    customer_area = models.ForeignKey("area.Area", on_delete=models.PROTECT)
    customer_address = models.CharField(max_length=100)
    item_type = models.ForeignKey(
        ItemType, on_delete=models.SET_NULL, null=True, blank=True)
    item_description = models.CharField(max_length=100, blank=True, null=True)
    item_weight = models.CharField(max_length=50, default='1KG')
    instruction = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['creationDate', ]
        # unique_together = (("parcel_id", "customer_phone"),)

    def __str__(self):
        return self.parcel_id


class OrderCost(models.Model):
    """
    Money that the merchant owner will give to the courier for delivery
    """
    delivery_charge = models.DecimalField(max_digits=4, decimal_places=2)
    cod_fee = models.DecimalField(max_digits=4, decimal_places=2)
    discounts = models.DecimalField(max_digits=4, decimal_places=2)
    additional_charge = models.DecimalField(max_digits=4, decimal_places=2)
    total = models.DecimalField(max_digits=4, decimal_places=2)
    order = models.OneToOneField(ParcelOrder, on_delete=models.CASCADE)


class Delivery(models.Model):
    PICKUP_STATUS_PENDING = 'P'
    PICKUP_STATUS_ASSIGNED = 'A'
    PICKUP_STATUS_PICKED = 'K'
    PICKUP_STATUS_CANCELED = 'C'
    PICKUP_STATUS_RECEIVED = 'R'  # Received at sorting zone
    DELIVERY_STATUS_NULL = 'N'
    DELIVERY_STATUS_TRANSIT = 'T'  # In transit to last hub
    # Reached last hub, Out for delivery, assigned to delivery man
    DELIVERY_STATUS_ASSIGNED = 'D'
    DELIVERY_STATUS_RETURN = 'X'  # Exit
    DELIVERY_STATUS_COMPLETE = 'H'  # Happy_
    DELIVERY_STATUS_RETURNED = 'S'  # SAD

    PICKUP_STATUS_CHOICES = [
        (PICKUP_STATUS_PENDING, 'Pending'),
        (PICKUP_STATUS_ASSIGNED, 'Assigned'),
        (PICKUP_STATUS_PICKED, 'Picked'),
        (PICKUP_STATUS_CANCELED, 'Canceled'),
        (PICKUP_STATUS_RECEIVED, 'Received'),
    ]
    DELIVERY_STATUS_CHOICES = [
        (DELIVERY_STATUS_NULL, 'No Data'),
        (DELIVERY_STATUS_TRANSIT, 'In Transit'),
        (DELIVERY_STATUS_ASSIGNED, 'Assigned'),
        (DELIVERY_STATUS_RETURN, 'Returning'),
        (DELIVERY_STATUS_COMPLETE, 'Complete')
    ]

    parcel = models.OneToOneField(ParcelOrder, on_delete=models.CASCADE)
    pickupman = models.ForeignKey(
        'profiles.DeliveryMan', related_name="pickups", on_delete=models.SET_NULL, null=True, blank=True)

    pickup_status = models.CharField(
        max_length=1, choices=PICKUP_STATUS_CHOICES, default=PICKUP_STATUS_PENDING)
    delivery_status = models.CharField(
        max_length=1, choices=DELIVERY_STATUS_CHOICES, default=DELIVERY_STATUS_NULL)
    current_hub = models.ForeignKey(
        "area.Hub", related_name='stored_deliveries', on_delete=models.CASCADE, null=True, blank=True)
    destination_hub = models.ForeignKey(
        "area.Hub", related_name='deliveries', on_delete=models.CASCADE)  # auto add percel delivery area
    deliveryman = models.ForeignKey(
        'profiles.DeliveryMan', related_name="deliveries", on_delete=models.SET_NULL, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)


class ParcelIssue(models.Model):
    ISSUE_OPEN = 'O'
    ISSUE_CLOSED = 'C'
    ISSUE_CHOICES = [
        (ISSUE_OPEN, 'Open'),
        (ISSUE_CLOSED, 'Closed')
    ]

    last_update = models.DateTimeField(auto_now=True)
    issue_status = models.CharField(
        max_length=1, choices=ISSUE_CHOICES, default=ISSUE_OPEN)
    issue_for = models.ForeignKey(
        ParcelOrder, related_name="issue", on_delete=models.CASCADE)
    issue_description = models.TextField(null=True, blank=True)
    issue_response = models.TextField(null=True, blank=True)


# Merchant
class AccountReceivable(models.Model):
    """
    Amount of money courier will receive.
    - Delivery Fees Paid by the merchant
    """
    due_amount = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.0)
    merchant = models.OneToOneField(
        "profiles.Merchant", on_delete=models.CASCADE)


class Payment(models.Model):
    """
    Amount of money to pay the merchant
    """
    pending = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    delivery_due = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.0)
    inprocess = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.0)
    processed = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.0)
    merchant = models.OneToOneField(
        "profiles.Merchant", on_delete=models.CASCADE)


class Invoice(models.Model):
    payment_to = models.OneToOneField(
        "profiles.Merchant", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    date = models.DateTimeField(auto_now=True)
