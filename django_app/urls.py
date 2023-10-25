from django.urls import path
from django_app.views import *



urlpatterns = [
    path('calculararea/',calculararea),
    path('sobre/', sobre),
    path('informacoes/creditocarbono/', infocredito),
    path('',home),
]
