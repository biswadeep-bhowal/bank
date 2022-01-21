from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', views.Home, name = 'home' ),
    path( 'transaction/', include( 'transaction.urls' ) ),
    path( 'user/', include( 'user.urls' ) )
]

urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )