from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/listings/listings.html')


def search(request):
    return HttpRequest('')


def listing(request, id):
    return render(request, 'pages/listings/listing.html')