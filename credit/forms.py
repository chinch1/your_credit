from django import forms
from django.forms import ModelForm
from credit.models import Credit


class CreditForm(ModelForm):
    class Meta:
        model = Credit
        fields = ['client', 'bank', 'description', 'minimal_amount',
                  'maximal_amount', 'loam_term', 'type']
        widgets = {
            'client': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Client',
                'style': 'width: 300px'
            }),
            'bank': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Bank',
                'style': 'width: 300px'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                'style': 'width: 300px'
            }),
            'minimal_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minimal Amount',
                'style': 'width: 300px'
            }),
            'maximal_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maximal Amount',
                'style': 'width: 300px'
            }),
            'loam_term': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Loam Term',
                'style': 'width: 300px'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Type',
                'style': 'width: 300px'
            }),
        }
