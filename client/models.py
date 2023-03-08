from django.db import models
from bank.models import Bank
# Create your models here.


class Client(models.Model):

    class ClientType(models.TextChoices):
        NATURAL = 'Natural'
        JURIDICO = 'Juridico'

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField(null=False)
    age = models.IntegerField()
    nationality = models.CharField(max_length=20)
    billing_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, unique=True, null=False)
    phone_number = models.CharField(max_length=20, unique=True)
    type = models.CharField(
        max_length=10, choices=ClientType.choices, default=ClientType.NATURAL)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated_at', 'created_at']

    def __str__(self):
        return self.full_name
