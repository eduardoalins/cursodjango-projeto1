from django.urls import path
from django_app.views import home, sobre



urlpatterns = [
    path('',home),
    path('sobre/', sobre),
]
