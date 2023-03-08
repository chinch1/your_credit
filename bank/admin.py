from django.contrib import admin
from bank.models import Bank

# Register your models here.


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'type')
