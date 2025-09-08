"""
URL configuration for Encargo4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from core.views import index, forowiki, login, registro, cuenta, recuperar, animales, armas, construcciones, consumibles, enemigos, flora, historia, logros, lugares

urlpatterns = [
    path("", index, name="menuprincipal"),

    path("usuarios/", forowiki, name="forowiki"),
    path("usuarios/", login),
    path("usuarios/", registro),
    path("usuarios/", cuenta),
    path("usuarios/", recuperar),
    
    path("categorias/", animales, name="animales"),
    path("categorias/", armas, name="armas"),
    path("categorias/", construcciones, name="construcciones"),
    path("categorias/", consumibles),
    path("categorias/", enemigos),
    path("categorias/", flora),
    path("categorias/", historia),  
    path("categorias/", logros),
    path("categorias/", lugares)
]
