from django.contrib import admin
from credit.models import Credit
# Register your models here.


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'bank_id', 'description', 'minimal_amount',
                    'maximal_amount', 'loam_term', 'register_date', 'type')
