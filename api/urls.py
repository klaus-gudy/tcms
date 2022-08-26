from django.urls import path
from . import views
urlpatterns = [
    path('', views.getBooks),
    path('book/create/', views.createBook),
    path('book/<str:pk>/update/', views.updateBook),
    path('book/<str:pk>/', views.getDetailBook),
    path('book/<str:pk>/delete/', views.deleteBook)
]