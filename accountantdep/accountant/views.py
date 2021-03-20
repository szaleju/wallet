from django.shortcuts import render, redirect
from .models import Asset, AccountPln
from .forms import AddTransactionForm, UpdateBalanceForm


def accountant_view(request):
    queryset = Asset.objects.all()
    transaction_form = AddTransactionForm()
    balance_form = UpdateBalanceForm()
    balance = AccountPln.objects.last()
    if request.method=='POST':
        balance_form = UpdateBalanceForm(request.POST)
        if balance_form.is_valid():
            last_transaction = AccountPln.objects.last()
            print("LAST TOTAL BALANCE: ", last_transaction.total_balance)
            total_balance = last_transaction.total_balance
            balance_update = balance_form.cleaned_data['balance']
            transaction_type = balance_form.cleaned_data['transaction_type']
            if transaction_type=='deposit':
                total_balance = total_balance + balance_update
            else:
                total_balance = total_balance - balance_update
            AccountPln.objects.create(
                balance=balance_update, 
                transaction_type=transaction_type,
                total_balance=total_balance,
            )
            return redirect('accountant:accountant')
    context = {
        'asset_list': queryset,
        'balance': balance,
        'transaction_form': transaction_form,
        'balance_form': balance_form,
    }
    return render(request, 'accountant/accountant.html', context)
