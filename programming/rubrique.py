# Dans programming/rubrique.py

from django.db import models

class RubriqueModel(models.Model):  # Renommez le modèle ici
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
