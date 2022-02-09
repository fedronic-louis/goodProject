"""lab URL Configuration

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
from django.urls import path, include

from . import views

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.home, name='home'),
    path('list', views.lab_list, name='lab_list'),
    path('lab_views/<pk>', views.lab_views, name='lab_views'),
    path('add', views.lab_create, name='lab_create'),
    path('update/<pk>', views.lab_update, name='lab_update'),
    path('delete/<pk>', views.lab_delete, name='lab_delete'),

]
