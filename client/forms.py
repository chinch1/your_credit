from django import forms
from django.forms import ModelForm, DateInput, EmailInput, NumberInput, TextInput, Select
from client.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['bank', 'full_name', 'birthday', 'age', 'nationality',
                  'billing_address', 'email', 'phone_number', 'type']
        widgets = {
            'bank': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Bank',
                'style': 'width: 300px'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
                'style': 'width: 300px'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Birthday',
                'style': 'width: 300px'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age',
                'style': 'width: 300px'
            }),
            'nationality': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nationality',
                'style': 'width: 300px'
            }),
            'billing_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Billing Address',
                'style': 'width: 300px'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'style': 'width: 300px'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'style': 'width: 300px'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Type',
                'style': 'width: 300px'
            }),
        }

    birthday = forms.DateTimeField(
        label="Birthday", widget=forms.DateInput(attrs={'type': 'date'}))
