from django.shortcuts import render
from django.http import HttpResponse
from .models import Empresas
# Create your views here.

def calculararea (request):
    return render(request, 'calculararea.html')

def sobre (request):
    return HttpResponse("Sobre nozes!")

def infocredito (request):
    return render(request, 'infocredito.html')

def home (request):
    return render(request, 'home.html')

def empresasprox (request):
    return render(request, 'empresasprox.html')

def teste (request):
    return render(request, 'teste.html')

def add_empresas(request):
    nova = Empresas()
    nova_nome = request.POST.get('nome')
    nova_rua = request.POST.get('rua')
    nova.save()

    add_empresas = {
        'add_empresas': Empresas.objects.all()
    }
    
    return render(request, 'teste2.html', Empresas)