# Dans programming/author.py

from django.db import models

class AuthorModel(models.Model):  # Renommez le modèle ici
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name
