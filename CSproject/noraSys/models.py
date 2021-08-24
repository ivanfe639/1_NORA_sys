from django.db import models
from django.db.models.base import ModelState

# Create your models here.

class SuperUsuario(models.Model):
    USER = models.CharField(max_length=30)
    PASSWORD = models.CharField(max_length=50)  

class Menu(models.Model):
    DATE = models.DateField()
    OPTION1 = models.CharField(max_length=50)
    OPTION2 = models.CharField(max_length=50)
    OPTION3 = models.CharField(max_length=50)
    OPTION4 = models.CharField(max_length=50)

class Pedido(models.Model):
    DATE = models.DateField()
    NAME = models.CharField(max_length=50)
    OPTION = models.IntegerField()
    COMMENTS = models.CharField(max_length=150)