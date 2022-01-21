from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from transaction import Transaction
from user import Customer


def Login( request ) :
    
    if request.method == 'POST' : pass

    
    return render( request, 'login.html', {} )


def Register( request ) :
    
    if request.method == 'POST' : pass

    
    return render( request, 'register.html', { 'title' : 'Register | Bank' } )