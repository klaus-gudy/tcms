from django.urls import path
from .views import *

urlpatterns = [
    path('', DepositListView.as_view(), name='deposit_list'),    
]