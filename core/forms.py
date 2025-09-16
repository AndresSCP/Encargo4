from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            auth_login(request, user)
            return redirect('menuprincipal')  # redirige al inicio después del login
    else:
        formulario = AuthenticationForm()
    
    context = {
        'formulario': formulario
    }
    return render(request, 'usuarios/inicio_sesion_wiki.html', context)