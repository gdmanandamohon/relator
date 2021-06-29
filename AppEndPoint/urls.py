from django.shortcuts import redirect
from django.urls.conf import include
from Listings.models import Listing
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views 


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('listings/', include('Listings.urls')),
]
