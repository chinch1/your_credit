from rest_framework.routers import DefaultRouter
from client.api.views import ClientApiViewSet

router_clients = DefaultRouter()

router_clients.register(r'client', ClientApiViewSet, 'client')
