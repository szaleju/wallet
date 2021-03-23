from django.shortcuts import render, redirect
from .models import Asset, AccountPln
from .forms import AddTransactionForm, UpdateBalanceForm


def process_balance_update(form, last_transaction, submit_value):
    total_balance = last_transaction.total_balance
    if submit_value == 'Send transaction':
        balance_update = form.cleaned_data['price']*form.cleaned_data['quantity']
    else:
        balance_update = form.cleaned_data['balance']
    transaction_type = form.cleaned_data['transaction_type']
    if transaction_type=='deposit' or transaction_type=='sell':
        total_balance = total_balance + balance_update
    else:
        total_balance = total_balance - balance_update
    AccountPln.objects.create(
        balance=balance_update, 
        transaction_type=transaction_type,
        total_balance=total_balance,
    )


def process_transaction(form, last_transaction, submit_value):
    asset = form.cleaned_data['asset']
    quantity = form.cleaned_data['quantity']
    transaction_type = form.cleaned_data['transaction_type']
    owned_asset = Asset.objects.filter(asset=asset).first()
    if owned_asset:
        if transaction_type == 'buy':
            owned_asset.quantity += quantity
        else:
            print("ELSE!")
            owned_asset.quantity -= quantity
        owned_asset.save()
    else:
        Asset.objects.create(asset=asset, quantity=quantity)
    process_balance_update(form, last_transaction, submit_value)


def accountant_view(request):
    queryset = Asset.objects.all()
    transaction_form = AddTransactionForm()
    balance_form = UpdateBalanceForm()
    balance = AccountPln.objects.last()
    if request.method=='POST':
        submit_value = request.POST.get('submit')
        last_transaction = AccountPln.objects.last()
        if submit_value == 'Update balance':
            form = UpdateBalanceForm(request.POST)
        elif submit_value == 'Send transaction':
            form = AddTransactionForm(request.POST)
        if  form.is_valid() and submit_value == 'Update balance':
            process_balance_update(form, last_transaction, submit_value)
            return redirect('accountant:accountant')
        elif  form.is_valid() and submit_value == 'Send transaction':
            process_transaction(form, last_transaction, submit_value)
            return redirect('accountant:accountant')
    context = {
        'asset_list': queryset,
        'balance': balance,
        'transaction_form': transaction_form,
        'balance_form': balance_form,
    }
    return render(request, 'accountant/accountant.html', context)
