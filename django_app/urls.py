from django.urls import path
from django_app.views import calculararea, sobre, infocredito



urlpatterns = [
    path('calculararea/',calculararea),
    path('sobre/', sobre),
    path('informacoes/creditocarbono/', infocredito),
]
