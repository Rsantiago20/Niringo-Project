from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h3>Bienvenidos a nuestro primero proyecto Niringo's Store</h3")

def catalogo(request):
    return HttpResponse("<h3>Bienvenido al cátalogo de juegos</h3>")

def carrito(request):
    return HttpResponse("<h3>Bienvenido al carrito</h3>")
# Create your views here.