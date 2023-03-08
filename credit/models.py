from django.db import models
from client.models import Client
from bank.models import Bank

# Create your models here.


class Credit(models.Model):
    class CreditType(models.TextChoices):
        AUTOMOTRIZ = 'Automotriz'
        HIPOTECARIO = 'Hipotecario'
        COMERCIAL = 'Comercial'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=False)
    minimal_amount = models.FloatField(null=False)
    maximal_amount = models.FloatField(null=False)
    loam_term = models.IntegerField(null=False)
    register_date = models.DateField(auto_now=True)
    type = models.CharField(
        max_length=12, choices=CreditType.choices, default=CreditType.COMERCIAL)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated_at', 'created_at']

    def __str__(self):
        return self.description
