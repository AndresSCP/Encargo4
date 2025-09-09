from django.shortcuts import render

def index(request):
    return render(request, 'menuprincipal_wiki.html')

def forowiki(request):
    return render(request, 'usuarios/forowiki.html')

def login(request):
    return render(request, 'usuarios/inicio_sesion_wiki.html')

def registro(request):
    return render(request, 'usuarios/registrase_wiki.html')

def cuenta(request):
    return render(request, 'usuarios/micuentatf.html')

def recuperar(request):
    return render(request,'usuarios/recuperarcontra.html')

def animales(request):
    return render(request, 'categorias/Animales.html')

def armas(request):
    return render(request, 'categorias/Armas.html')

def construcciones(request):
    return render(request, 'categorias/Construcciones.html')

def consumibles(request):
    return render(request, 'categorias/Consumibles.html')

def enemigos(request):
    return render(request, 'categorias/Enemigos.html')

def flora(request):
    return render(request, 'categorias/Flora.html')

def historia(request):
    return render(request, 'categorias/historia.html')

def logros(request):
    return render(request, 'categorias/Logros.html')

def lugares(request):
    return render(request, 'categorias/Lugarestf.html')







