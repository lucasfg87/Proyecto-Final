from django.db import models

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
      return f"{self.id} , {self.nombre}, {self.numero_pasaporte}, "


class Autos(models.Model):

    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    año = models.IntegerField()
    
    def __str__(self):
      return f"{self.id} , {self.marca}, {self.modelo}, "

class Vinos(models.Model):

    marca = models.CharField(max_length=100)
    provincia = models.CharField(max_length=200)
    año = models.IntegerField()
    
    def __str__(self):
      return f"{self.id} , {self.marca}, {self.año}, "

