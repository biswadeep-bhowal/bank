from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


def Login( request ) : return render( request, 'login.html', {} )


def Register( request ) : return render( request, 'register.html', {} )


def Profile( request ) : return render( request, 'profile.html', {} )