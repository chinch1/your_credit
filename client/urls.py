from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('get/<str:pk>/', views.showClient, name='show_client'),
    path('list/', views.listClients, name='list_client'),
    path('create/', views.createClient, name='create-client'),
    path('update/<str:pk>/', views.updateClient, name='update_client'),
    path('delete/<str:pk>/', views.deleteClient, name='delete_client'),
]
