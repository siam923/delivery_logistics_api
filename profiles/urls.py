from django.urls import path
from . import views

urlpatterns = [
    path('merchants/', views.MerchantList.as_view()),
    path('merchants/<int:pk>', views.MerchantDetail.as_view()),
]
