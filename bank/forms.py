from django import forms
from django.forms import ModelForm, TextInput, Select
from bank.models import Bank


class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'address', 'type']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'style': 'width: 300px',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address',
                'style': 'width: 300px'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Type',
                'style': 'width: 300px'
            }),
        }
