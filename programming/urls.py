from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:article_id>/', views.article_detail, name='programming_article_detail'),
    path('articles/', views.article_list, name='programming_article_list'),
]
