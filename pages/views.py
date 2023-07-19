from django.shortcuts import render
from .models import *

def home(request):
    home1s = home1.objects.all()
    context = {
        'home1s': home1s
    }
    return render(
        request,
        'pages/home.html',
        context
    )

def avtomobil(request):
    repairs = repair.objects.all()
    context = {
        'repairs': repairs
    }
    return render(
        request,
        'pages/avtomobil.html',
        context
    )

def sport(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(
        request,
        'pages/sport.html',
        context
    )

def smartfon(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(
        request,
        'pages/smartfon.html',
        context
    )

def notebuk(request):
    models = model.objects.all()
    context = {
        'models': models
    }
    return render(
        request,
        'pages/notebuk.html',
        context
    )
