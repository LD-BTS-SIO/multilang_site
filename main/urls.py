from django.urls import path
from .views import article_list  # Assurez-vous que le chemin est correct

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    # Autres URLs de votre application main
]
