from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from transaction import Transaction
from user import Customer

def Home( request ) : return render( request, 'home.html', { 'title' : 'Home | Bank' } )


def Login( request ) :
    
    if request.method == 'POST' : pass

    
    return render( request, 'login.html', {} )


def Register( request ) : 
    
    if request.method == 'POST' : pass

    
    return render( request, 'register.html', { 'title' : 'Register | Bank' } )


def Transfer( request ) : return render( request, 'transfer.html', {} )


def Deposit( request ) : return render( request, 'deposit', {} )


def Withdraw( request ) : return render( request, 'withdraw.html', {} )