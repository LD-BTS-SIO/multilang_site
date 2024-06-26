# myapp/models.py
from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rubrique(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

