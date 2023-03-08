from django.urls import path, include
from . import views

urlpatterns = [
    path('get/<str:pk>/', views.showBank, name='show_bank'),
    path('list/', views.listBanks, name='list_bank'),
    path('create/', views.createBank, name='create-bank'),
]
