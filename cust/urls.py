from django.urls import path
from .views import *

urlpatterns = [
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('customer/update/<str:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/detail/<str:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/delete/<str:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    
]