from django.db import models

class Organizador(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - {self.organizador}'
