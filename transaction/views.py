from django.shortcuts import render, redirect
from user.models import Customer
from .models import Transaction

def Deposit( request ) : 
    
    customer = Customer.objects.get( user = request.user )

    if request.method == 'POST' : 
        
        try : 
            
            amount = int( request.POST[ 'amount' ] )
            if amount < 1 : raise Exception( 'Invalid Amount..' ) 

            customer.balance = customer.balance + amount
            customer.save()

            return render( request, 'deposit.html', { 'customer' : customer } )

        except : return render( request, 'deposit.html', { 'customer' : customer, 'Failed' : True } )

    return render( request, 'deposit.html', { 'customer' : customer } )


def Withdraw( request ) : 

    customer = Customer.objects.get( user = request.user )

    if request.method == 'POST' : 
        
        try : 
            
            amount = int( request.POST[ 'amount' ] )
            
            if amount > customer.balance or amount < 1 : raise Exception( 'Invalid Amount' )

            customer.balance = customer.balance - amount
            customer.save()

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

            return render( request, 'transfer.html', { 'customer' : customer } )

        except : return render( request, 'transfer.html', { 'customer' : customer, 'Failed' : True } )

    return render( request, 'transfer.html', { 'customer' : customer } )


def Transactions( request ) : return render( request, 'transactions.html', {} )