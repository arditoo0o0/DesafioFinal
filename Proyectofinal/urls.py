
from django.contrib import admin
from django.urls import path
from Proyectofinalapp.views import Perfiles,inicio,cursos
from Registroapp.views import Perfiles,Primeravista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Perfiles/',Perfiles, name="Perfiles"),
    path('Inicio',inicio, name='inicio'),
    path('Cursos',cursos, name="Cursos"),
    path('',Primeravista , name="Primeravista")
]
