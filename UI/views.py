from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    #return HttpResponse("About")
    return render(request, 'pages/about.html')


def listings(request):
    return render(request, 'pages/listings.html')

def listing(request, listing_id):
    return render(request, 'pages/listing.html')

def search(request, listing_id):
    return render(request, 'pages/search.html')

def login(request):
    return HttpResponse("")

def register(request):
    return HttpResponse("")
