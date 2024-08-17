from django.contrib import admin
from .models import Alumno,Profesor

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Profesor)