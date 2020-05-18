from django.db import models
from django.utils import timezone

# Create your models here.

class personas(models.Model):
    id_personas = models.AutoField(primary_key = True, null = False)
    descripcion = models.CharField(max_length = 30)
    correo = models.EmailField()
    celular = models.IntegerField()

class tpo_articulo(models.Model):
    id_tpo_articulo = models.AutoField(primary_key = True, null = False)
    descripcion = models.CharField(max_length = 20)

class articulos(models.Model):
    id_articulos = models.AutoField(primary_key = True, null = False)
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to= 'imagenes/')
    tipo = models.ForeignKey(tpo_articulo, on_delete = models.CASCADE)

class precios(models.Model):
    id_precios = models.AutoField(primary_key = True, null = False)
    importe = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateTimeField(auto_now = True)
    tipo_lista = models.CharField(max_length = 9, default = 'minorista')
    articulo = models.ForeignKey(articulos, on_delete = models.CASCADE)
