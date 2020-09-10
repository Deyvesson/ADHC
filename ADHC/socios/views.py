from django.shortcuts import render
from django.http import HttpResponse

def listaSocios(request):
    return render(request, 'socios/lista.html')
