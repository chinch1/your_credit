from rest_framework.routers import DefaultRouter
from credit.api.views import CreditApiViewSet

router_credits = DefaultRouter()

router_credits.register(r'credit', CreditApiViewSet, 'credit')
