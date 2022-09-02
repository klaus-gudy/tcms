from django.urls import path

# from .base.views import *
from api.base import views
from .cust.views import CustomerCreateAPIView,CustomerListAPIView


urlpatterns = [
    path('book/list/', views.getBooks),
    path('book/create/', views.createBook),
    path('book/<str:pk>/update/', views.updateBook),
    path('book/<str:pk>/', views.getDetailBook),
    path('book/<str:pk>/delete/', views.deleteBook),

    path('customer/create/', CustomerCreateAPIView.as_view(), name='cust-create'),
    path('customer/list/', CustomerListAPIView.as_view(), name='cust-list'),
]