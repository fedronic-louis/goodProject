"""formation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    path('commercial/', include(('commercial.urls', 'commercial'), namespace='commercial')),
    path('produit/', include(('produit.urls', 'produit'), namespace='produit')),
    path('lab/', include(('lab.urls', 'lab'), namespace='lab')),
    path('pedago/', include(('pedago.urls', 'pedago'), namespace='pedago')),
    path('administration/', include(('administration.urls', 'administration'), namespace='administration')),
    path('', views.home, name='home'),
]
