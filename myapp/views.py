from django.shortcuts import render, get_object_or_404
from .models import Rubrique, Author, Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

def index(request):
    return render(request, 'main/index.html')

def rubrique_list(request):
    rubriques = Rubrique.objects.all()
    return render(request, 'main/rubrique_list.html', {'rubriques': rubriques})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'main/author_list.html', {'authors': authors})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'main/article_detail.html', {'article': article})
