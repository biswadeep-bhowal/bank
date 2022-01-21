from django.urls import path
from . import views

urlpatterns = [
    path( 'deposit', views.Deposit, name = 'deposit' ),
    path( 'withdraw', views.Withdraw, name = 'withdraw' ),
    path( 'transfer', views.Transfer, name = 'transfer' )
]