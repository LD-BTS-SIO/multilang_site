from django.contrib import admin
# cybersecurite/admin.py

from .models import Article, Author, Rubrique


# Assurez-vous qu'il n'y a qu'un seul enregistrement de ce modèle
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Rubrique)