from django.urls import path
from .views import StoreList, CustomerList, OrderCostList, MerchantStoreList, PickupAddressList, DeliveryTypeList, ItemTypeList, ParcelOrdersAll, DeliveryList, DeliveryDetail

urlpatterns = [
    # path('<int:pk>/', StoreList.as_view()), # merchant(pk) stores
    path('stores/', StoreList.as_view()),
    path('merchants/<int:pk>/stores', MerchantStoreList.as_view()),
    path('stores/<int:pk>/pickupaddress/list', PickupAddressList.as_view()),
    path('deliverytypes/', DeliveryTypeList.as_view()),
    path('itemtypes/', ItemTypeList.as_view()),
    path('parcels/create', ParcelOrdersAll.as_view()),
    path('customers/', CustomerList.as_view()),
    path('parcels/<int:pk>/order/', OrderCostList.as_view()),
    path('parcels/<int:pk>/delivery/list/', DeliveryList.as_view()),
    path('parcels/<int:parcel_id>/delivery/<int:pk>/', DeliveryDetail.as_view()),

]
