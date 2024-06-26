from django.urls import path
from . import views

urlpatterns = [
     path('articles/', views.article_list, name='cybersecurite_article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='cybersecurite_article_detail'),
]
