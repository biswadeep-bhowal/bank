from django.shortcuts import render, redirect
from user.models import Customer
from .models import Transaction

def Deposit( request ) : return render( request, 'deposit.html', {} )

def Withdraw( request ) : return render( request, 'withdraw.html', {} )

def Transfer( request ) : return render( request, 'transfer.html', {} )

def Transactions( request ) : return render( request, 'transactions.html', {} )