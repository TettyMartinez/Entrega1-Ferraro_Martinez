from django.db import models

# Create your models here.

class Atleta(models.Model):

    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    deporte = models.IntegerField()

class Coach(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField

class Club(models.Model):
    nombre = models.CharField(max_length=40)
    division= models.CharField(max_length=40)
    años= models.IntegerField ()