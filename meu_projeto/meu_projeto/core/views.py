from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Olá Mundo! Esta é a minha página home")