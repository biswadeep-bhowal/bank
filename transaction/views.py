from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
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


def Transactions( request ) :  
    
    customer = Customer.objects.get( user = request.user )
    transactions = Transaction.objects.filter( Q( sender = customer.user.id ) | Q( receiver = customer.user.id ) )

    T = []

    for i in transactions : 

        i = list( map( int, str( i ).split() ) )

        if i[ 1 ] == customer.user.id :     

            if i[ 2 ] == 3 :    T.append( [ i[ 0 ], "Withdrawal", "-{}".format( i[ 3 ] ), False ] )
            elif i[ 2 ] == 4 :  T.append( [ i[ 0 ], "Deposit", "+{}".format( i[ 3 ] ), True ] )
            else :              T.append( [ i[ 0 ], User.objects.get( id = i[ 2 ] ).get_full_name(), "-{}".format( i[ 3 ] ), False ] )

        elif i[ 2 ] == customer.user.id : T.append( [ i[ 0 ], User.objects.get( id = i[ 1 ] ).get_full_name(), "+{}".format( i[ 3 ] ), True ] )


    return render( request, 'transactions.html', { 'customer' : customer, 'transactions' : T } )