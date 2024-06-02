from django.db import models

class TagCloth(models.Model):
    name = models.CharField(max_length=50)

class Cloth(models.Model):
    name = models.CharField(max_length=100)
    tag = models.ForeignKey(TagCloth, on_delete=models.CASCADE)
    colour = models.CharField(max_length=100, verbose_name='Укажите цвет')