from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
import random


def Login( request ) : 
    
    if request.method == 'POST' : 

        user = authenticate( username = request.POST[ 'username' ], password = request.POST[ 'password' ] )

        if user is not None : 
            login( request, user )
            return redirect( 'http://localhost:8000/' )

        else : return render( request, 'login.html', { 'Failed' : True } )
    
    
    return render( request, 'login.html', {} )


def Register( request ) : return render( request, 'register.html', {} )


def Profile( request ) : return render( request, 'profile.html', { 'customer' : Customer.objects.get( user = request.user ) } )