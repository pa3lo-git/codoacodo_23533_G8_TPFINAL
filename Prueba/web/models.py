from django.db import models

# Create your models here.

class Receta(models.Model):
    Nombre = models.CharField(max_length=30, verbose_name='Nombre')
    Descripcion = models.CharField(max_length=150, verbose_name='Descripcion', null=True)
    Imagen = models.ImageField(upload_to='')
    Ingredientes = models.CharField(max_length=300, verbose_name='Ingredientes')
    Preparacion = models.CharField(max_length=500, verbose_name='Preparacion')