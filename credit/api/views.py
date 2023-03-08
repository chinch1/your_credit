from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from credit.models import Credit
from credit.api.serializers import CreditSerializer


class CreditApiViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):

    def get_queryset(self):
        return Credit.objects.all()

    def get_serializer_class(self):
        return CreditSerializer
