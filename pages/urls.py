from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('avtomobil/', avtomobil, name='avtomobil'),
    path('sport/', sport, name='sport'),
    path('Smartfon/', smartfon, name='smartfon'),
    path('notebuk/', notebuk, name='notebuk'),
] 
