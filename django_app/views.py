from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculararea (request):
    return render(request, 'calculararea.html')

def sobre (request):
    return HttpResponse("Sobre nozes!")

def infocredito (request):
    return render(request, 'infocredito.html')