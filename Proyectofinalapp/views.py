from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,'Proyectofinalapp/inicio.html')

def Perfiles(request):
    return render(request,'Registroapp/Perfiles.html')

def cursos(request):
    return render(request,'Proyectofinalapp/Cursos.html')
def acercademi(request):
    return render(request,'Proyectofinalapp/acercademi.html')
