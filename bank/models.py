from django.db import models
# Create your models here.


class Bank(models.Model):
    class BankType(models.TextChoices):
        PRIVADO = 'Privado'
        GOBIERNO = 'Gobierno'

    name = models.CharField(max_length=50, null=False, unique=True)
    address = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=BankType.choices,
        default=BankType.PRIVADO,
        null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated_at', 'created_at']

    def __str__(self):
        return self.name
