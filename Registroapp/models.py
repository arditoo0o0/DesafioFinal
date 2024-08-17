from django.db import models

class Alumno(models.Model):
    Usuario=models.CharField(max_length=40)
    Contraseña=models.CharField(max_length=40)
    Gmail=models.CharField(max_length=40)
    


class Profesor(models.Model):
    Usuario=models.CharField(max_length=40)
    Contraseña=models.CharField(max_length=40)
    Gmail=models.CharField(max_length=40)
    
 

    
class admin(models.Model):
    Usuario=models.CharField(max_length=40)
    Contraseña=models.CharField(max_length=40)
    Comision=models.CharField(max_length=40)
    
