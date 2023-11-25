from django.shortcuts import render, redirect
from .models import AccountBalance, Transaction
from decimal import Decimal
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    account_balance, created = AccountBalance.objects.get_or_create(pk=1)

    if request.method == 'POST':
        deposit_amt = Decimal(request.POST.get('deposit', 0))
        transfer_amt = Decimal(request.POST.get('transfer', 0))

        # Calculate the new balance
        new_balance = account_balance.balance + deposit_amt - transfer_amt
        account_balance.balance = new_balance
        account_balance.save()

        # Create a new transaction
        transaction = Transaction(deposit=deposit_amt, transfer=transfer_amt, new_balance=new_balance)
        transaction.save()

        # Associate the transaction with the account balance
        account_balance.transactions.add(transaction)

    context = {
        'deposit_amt': account_balance.balance,
        'transaction_history': account_balance.transactions.all()
    }
    return render(request, 'index.html', context)
