
from django.contrib import admin
from django.urls import path
from Proyectofinalapp.views import inicio,Perfiles,registro,cursos
from Registroapp.views import Perfiles
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Perfiles',Perfiles , name="Perfiles"),
    path('',inicio , name="inicio"),
    path('Cursos', curso , name="curso")
]
