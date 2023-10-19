from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    return render(request, 'home.html')

def sobre (request):
    return HttpResponse("Sobre nozes!")

def infocredito (request):
    return render(request, 'infocredito.html')