from django.db import models

# Create your models here.

class Cancion(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.CharField(max_length=50)
    artista = models.CharField(max_length=200)
    album = models.CharField(max_length=200)

