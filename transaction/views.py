from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import Customer
from .models import Transaction
import random

def Deposit( request ) : 
    
    customer = Customer.objects.get( user = request.user )

    if request.method == 'POST' : 
        
        try : 
            
            amount = int( request.POST[ 'amount' ] )
            if amount < 1 : raise Exception( 'Invalid Amount..' ) 

            customer.balance = customer.balance + amount
            customer.save()

            trans_id = random.randrange( 1000000000, 9999999999, 1 )
            sender = customer.user

            transaction = Transaction( trans_id = trans_id, amount = amount, sender = sender.id, receiver = 4 )
            transaction.save()

            return render( request, 'deposit.html', { 'customer' : customer } )

        except Exception as e: return render( request, 'deposit.html', { 'customer' : customer, 'Failed' : e } )

    return render( request, 'deposit.html', { 'customer' : customer } )


def Withdraw( request ) : 

    customer = Customer.objects.get( user = request.user )

    if request.method == 'POST' : 
        
        try : 
            
            amount = int( request.POST[ 'amount' ] )
            
            if amount > customer.balance or amount < 1 : raise Exception( 'Invalid Amount' )

            customer.balance = customer.balance - amount
            customer.save()

            trans_id = random.randrange( 1000000000, 9999999999, 1 )
            sender = customer.user

            transaction = Transaction( trans_id = trans_id, amount = amount, sender = sender.id, receiver = 3 )
            transaction.save()

            return render( request, 'withdraw.html', { 'customer' : customer } )

        except : return render( request, 'withdraw.html', { 'customer' : customer, 'Failed' : True } )

    return render( request, 'withdraw.html', { 'customer' : customer } )


def Transfer( request ) : 
    
    customer = Customer.objects.get( user = request.user )

    if request.method == 'POST' : 
        
        try : 
            
            amount = int( request.POST[ 'amount' ] )
            
            if not Customer.objects.filter( cust_id = int( request.POST[ 'cust_id' ] ) ).exists() : raise Exception( 'Invalid Customer ID..' )
            if amount > customer.balance or amount < 1 : raise Exception( 'Invalid Amount' )
            
            beneficiary = Customer.objects.get( cust_id = request.POST[ 'cust_id' ] )
            
            customer.balance = customer.balance - amount
            beneficiary.balance = beneficiary.balance + amount
            
            customer.save()
            beneficiary.save()

            trans_id = random.randrange( 1000000000, 9999999999, 1 )
            sender = customer.user
            receiver = beneficiary.user

            transaction = Transaction( trans_id = trans_id, amount = amount, sender = sender.id, receiver = receiver.id )
            transaction.save()            

            return render( request, 'transfer.html', { 'customer' : customer } )

        except Exception as e: return render( request, 'transfer.html', { 'customer' : customer, 'Failed' : e } )

    return render( request, 'transfer.html', { 'customer' : customer } )


def Transactions( request ) : return render( request, 'transactions.html', {} )