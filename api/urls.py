from django.urls import path

# from .base.views import *
from .cust.views import CustomerCreateAPIView,CustomerListAPIView


urlpatterns = [
    path('customer/create/', CustomerCreateAPIView.as_view(), name='cust-create'),
    path('customer/list/', CustomerListAPIView.as_view(), name='cust-list'),
]