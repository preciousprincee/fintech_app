
from django.db import models
from decimal import Decimal

class Transaction(models.Model):
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transfer = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    new_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)



class AccountBalance(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transactions = models.ManyToManyField(Transaction)

