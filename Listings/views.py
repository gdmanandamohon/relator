from django.http.request import HttpRequest
from UI.views import index
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/listings.html')


def search(request):
    return HttpRequest('')


def listing(request, id):
    return HttpRequest()