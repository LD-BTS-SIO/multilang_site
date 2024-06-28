= Compte rendu pour la création d'une application multilingue

:toc:

toc::[]
== (DARRAS Loïc )
== lien github : https://github.com/LD-BTS-SIO/multilang_site


=== Je tiens à préciser que j'ai fais ce projet sur VS CODE
:figure-caption!:

== I) Installation et Configuration de Django :

J'ai donc tout d'abord installé django :

Pour cela j'ai utilisé la commande "*pip install django*" :
====
image::assets\images\d1a.png[width=800, title="Installation de django", alt=""]
====


Ensuite j'ai créé le projet à l'aide de la commande suivantes : 

[source,lang]
----
django-admin startproject multilang_site
cd multilang_site

----


J'ai ensuite utilisé la commande *django-admin startproject* pour créer un nouveau projet Django nommé *multilang_site*.


J'ai ensuite crééé l'application main : 


[source,lang]
----
python manage.py startapp main
----


Il fuat ensuite ajouter l'Application à settings.py :
[source,lang]
----
INSTALLED_APPS = [
    ...
    'main',
]

MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
]

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
----


Configuration de l'url :

main/urls.py :

[source,lang]
----

from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
]


----



J'ai crééé ensuite des templates, des vues que je mettrai dans la partie finale du projet


Pour la partie *admin* de Django j'ai créé un superutilisateur: 
[source,lang]
----

python manage.py createsuperuser

----



J'ai aussi créé un  fichier requirements.txt :

[source,lang]
----
pip freeze > requirements.txt
----

Pour ajouter les migrations d'un projet on fait ceci : 

[source,lang]
----
python manage.py migrate


----


En conséquence, je peux ajouter des articles dans :  ajouter des articles : http://127.0.0.1:8000/admin/. qui est l'interface d'administration