from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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

def Logout( request ) : 

    logout( request )
    return redirect( 'http://localhost:8000/' )

def Register( request ) : 
    
    if request.method == 'POST' : 
        
        try : 

            first_name = request.POST[ 'first_name' ]
            last_name = request.POST[ 'last_name' ]

            username = request.POST[ 'username' ]
            password = request.POST[ 'password' ]
            confirm = request.POST[ 'confirm_password' ]

            search = User.objects.filter( username = username ).exists()
            if password != confirm or search is True : return render( request, 'register.html', { 'message' : 'Registration Unsuccessful...' } )

            user = User.objects.create_user( first_name = first_name, last_name = last_name, username = username, password = password )
            user.save()

            customer = Customer( cust_id = random.randrange( 1000001, 9999999, 1 ), user = user )
            customer.save()

            login( request, user )

            return redirect( 'http://localhost:8000/' )
        
        except Exception as e : return render( request, 'register.html', { 'message' : 'Registration Unsuccessful...' } )
    
    return render( request, 'register.html', {} )


def Profile( request ) : return render( request, 'profile.html', { 'customer' : Customer.objects.get( user = request.user ) } )