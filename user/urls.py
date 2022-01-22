from django.urls import path
from . import views

urlpatterns = [
    path( 'login/', views.Login, name = 'login' ),
    path( 'register/', views.Register, name = 'register' ),
    path( 'profile/', views.Profile, name  = 'profile' ),
    path( 'logout/', views.Logout, name = 'logout' )
]