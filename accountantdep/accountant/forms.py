from django import forms
from .models import Transaction, AccountPln


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'asset',
            'quantity',
            'price',
            'transaction_type',
        ]

        widgets = {
            'asset': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
        }


class UpdateBalanceForm(forms.ModelForm):
    class Meta:
        model = AccountPln
        fields = [
            'balance',
            'transaction_type',
        ]

        widgets = {
            'balance': forms.TextInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
        }