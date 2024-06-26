from django.db import models
from .author import Author  # Assurez-vous que le chemin est correct
from .rubrique import Rubrique  # Importez le modèle renommé

class Rubrique(models.Model):
    name = models.CharField(max_length=200)  # Renommé en "name" au lieu de "t"
    description = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

def default_author():
    return Author.objects.first()  # Cette fonction retourne le premier auteur existant, ajustez selon vos besoins

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=default_author)

    def __str__(self):
        return self.title
