from django.shortcuts import render

# Create your views here.

def index_estatico(request):
    return render(request, 'menuprincipal_wiki.html')

def inicio_sesion(request):
    return render(request, 'inicio_sesion_wiki.html')
