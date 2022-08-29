from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('books/update/<str:pk>/', BookUpdateView.as_view(), name='update'),
    path('books/detail/<str:pk>/', BookDetailView.as_view(), name='detail'),
    path('books/create/', BookCreateView.as_view(), name='create'),
    path('books/delete/<str:pk>/', BookDeleteView.as_view(), name='delete'),
]
