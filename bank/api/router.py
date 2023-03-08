from rest_framework.routers import DefaultRouter
from bank.api.views import BankApiViewSet

router_banks = DefaultRouter()

router_banks.register(r'bank', BankApiViewSet, 'bank')
