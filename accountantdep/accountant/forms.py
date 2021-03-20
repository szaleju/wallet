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

class UpdateBalanceForm(forms.ModelForm):
    class Meta:
        model = AccountPln
        fields = [
            'balance',
            'transaction_type',
        ]