from django.urls import path, include
from . import views

urlpatterns = [
    path('get/<str:pk>/', views.showCredit, name='show_credit'),
    path('list/', views.listCredits, name='list_credit'),
    path('create/', views.createCredit, name='create-credit'),
]
