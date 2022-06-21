from django.db import models

class Pizza(models.Model):
    nom = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=200)
    vegetarienne = models.BooleanField(default=False)
    prix = models.FloatField(default=0)

    def __str__(self):
        return self.nom

