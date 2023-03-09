from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h3>Bienvenidos a nuestro primero proyecto Niringo's Store</h3")
# Create your views here.