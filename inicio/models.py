from django.db import models

# Create your models here.

class Sugerencia(models.Model):
    titulo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(null=True)
    
    def __str__(self):
        return f"Titulo: {self.titulo} - Nombre: {self.nombre}"