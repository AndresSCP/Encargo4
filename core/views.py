from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


def index(request):
    return render(request, 'menuprincipal_wiki.html')

def forowiki(request):
    return render(request, 'usuarios/forowiki.html')

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasena = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasena)
            if usuario is None:
                context = {
                    'formulario': formulario,
                    'error': 'El usuario o la contraseña son incorrectos.'
                }
                return render(request, 'usuarios/inicio_sesion_wiki.html')
            else:
                auth_login(request, usuario)
                return redirect('menuprincipal')
        else:
            context = {
                'formulario': formulario
            }
            return render(request, 'usuarios/inicio_sesion_wiki.html', context)
           
    else:
        formulario = AuthenticationForm()
        context = {
        'formulario': formulario
    }
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







