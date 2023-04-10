from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=30)
    tipologia = models.CharField(max_length=30)
    superficie = models.FloatField()
    plantas = models.IntegerField()
    dormitorios = models.IntegerField()
    baños = models.IntegerField()

    
    def __str__(self):
        return f'Proyecto: {self.titulo} - Tipologia: {self.tipologia}'    