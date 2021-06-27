from django.urls import path
from django.urls.resolvers import URLPattern
from . import views 


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),

    path('listings', views.listings, name = 'listings'),
    path('listing/<listing_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search'),

]
