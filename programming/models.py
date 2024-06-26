from django.db import models
from .author import AuthorModel  # Assurez-vous que le chemin est correct
from .rubrique import RubriqueModel  # Importez le modèle renommé

class Rubrique(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)  # Ajoutez default=1 ici
    rubrique = models.ForeignKey(Rubrique, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
