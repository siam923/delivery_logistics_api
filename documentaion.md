### Library

djangorestframework, 'dj_rest_auth',

### Restrictions

No one can delete a Merchant, Store pickup address without deleting all the parcel orders by that store as models.PROTECT has been used.

Store code of the store model will be used with a specific pattern to generate the order id (consignment id) and the data will be tracked with the customer phone number and the order id.

On pickup receive update delivery status to transit.
is_picked = True
At delivery = False

On creating order.. send cost of delivery to payment table -> pending amount
after successfull delivery send to payment- delivery_due
during processing send to in_process
finally after processing -> processed
