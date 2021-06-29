from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    #return HttpResponse("About")
    return render(request, 'pages/about.html')

def login(request):
    return HttpResponse("")


def register(request):
    return HttpResponse("")


def listings(request):
    return render(request, 'pages/listings/listings.html')