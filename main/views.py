from django.shortcuts import render, get_object_or_404
from .models import Article  # Assurez-vous que le chemin vers votre modèle Article est correct

def article_list(request):
    articles = Article.objects.all()  # Récupère tous les articles
    return render(request, 'main/index.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)  # Récupère l'article spécifié par pk ou renvoie une erreur 404
    return render(request, 'main/article_detail.html', {'article': article})
