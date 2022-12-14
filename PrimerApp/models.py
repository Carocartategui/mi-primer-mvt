from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"


class Amigos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    anios_de_amistad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.id}"

class colegas(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_de_telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.id}"
