from django.urls import path
from django_app.views import home, sobre, infocredito



urlpatterns = [
    path('',home),
    path('sobre/', sobre),
    path('informacoes/creditocarbono/', infocredito),
]
