from django.urls import path
from django.urls.resolvers import URLPattern
from . import views 


# Route staarts with /listing
urlpatterns = [
    path('', views.index, name='listings'),
    path('listing/<listing_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search'),

]
