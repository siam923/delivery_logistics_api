from django.urls import path
from django.urls.conf import include
# from rest_framework_nested import DefaultRouter
from . import views


# router = DefaultRouter()
# router.register('district', views.AreaViewSet)


urlpatterns = [
    path('districts/', views.DistrictListView.as_view()),
    path('charges/', views.DeliveryChargeListView.as_view()),
    path('zones/', views.ZoneListView.as_view()),
    path('zones/<int:pk>/area/', views.AreaListView.as_view()),
]
