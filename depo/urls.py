from django.urls import path
from .views import *

urlpatterns = [
    path('history/', DepositListView.as_view(), name='deposit_list'),
    path('token/<str:pk>/', GenerateToken.as_view(), name='generate_token'),
    path('deposit/', DepositView.as_view(), name='deposit'),    
]