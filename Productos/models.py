from django.db import models


class productos(models.Model):

    nombre = models.CharField(max_length=20)
    calidad = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)