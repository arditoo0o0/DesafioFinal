from django.shortcuts import render
from django.http import HttpResponse

def Perfiles(request):
    return render(request,'registroapp/Perfiles.html')
def Primeravista(request):
    return render(request,'registroapp/Primeravista.html')
