from rest_framework.viewsets import ModelViewSet
from client.models import Client
from client.api.serializers import ClientSerializer


class ClientApiViewSet(ModelViewSet):

    def get_queryset(self):
        return Client.objects.all()

    def get_serializer_class(self):
        return ClientSerializer
