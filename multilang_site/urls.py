# C:\Users\darras\multilang_site\multilang_site\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Chemin vers l'interface d'administration
    path('', include('myapp.urls')),  # Inclut les URLs de myapp
     path('', include('blog.urls')),  # Inclure les URLs de l'application blog
     path('programming/', include('programming.urls')),
    path('cybersecurite/', include('cybersecurite.urls')),
]

