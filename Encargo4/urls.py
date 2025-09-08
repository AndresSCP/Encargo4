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

    path("usuarios/foro/", forowiki, name="forowiki"),
    path("usuarios/login/", login, name="login"),
    path("usuarios/registro/", registro, name="registrarse_wiki"),
    path("usuarios/cuenta/", cuenta, name="cuenta"),
    path("usuarios/recuperar/", recuperar, name="recuperar"),

    path("categorias/animales/", animales, name="animales"),
    path("categorias/armas/", armas, name="armas"),
    path("categorias/construcciones/", construcciones, name="construcciones"),
    path("categorias/consumibles/", consumibles, name="consumibles"),
    path("categorias/enemigos/", enemigos, name="enemigos"),
    path("categorias/flora/", flora, name="flora"),
    path("categorias/historia/", historia, name="historia"),  
    path("categorias/logros/", logros, name="logros"),
    path("categorias/lugares/", lugares, name="lugares"),
]
