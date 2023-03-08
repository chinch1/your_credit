from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from bank.models import Bank
from bank.api.serializers import BankSerializer


class BankApiViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):

    def get_queryset(self):
        return Bank.objects.all()

    def get_serializer_class(self):
        return BankSerializer
