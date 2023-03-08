from django.contrib import admin
from client.models import Client

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birthday', 'age', 'nationality',
                    'billing_address', 'email', 'phone_number', 'type')
