from django.shortcuts import render, redirect
from django.contrib import messages, auth
from mainapp.form import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def servicios(request):

    return render(request, 'servicios.html')

def empleos(request):

    return render(request, 'empleos.html')

def nosotros(request):

    return render(request, 'nosotros.html')

def contacto(request):

    return render(request, 'contacto.html')

def registro(request):

        # If the user is authenticated, redirect to the home page "inicio"
    if request.user.is_authenticated:
        return redirect('inicio')
    
    else:
        register_form = RegisterForm()

        # To save a new user through the form created in register. If the form is valid, save the user
        # The form method is set up to save the user directly in Django. If the user is created, it redirects you to the home page "inicio"
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                user = register_form.save()
                # Creation of the flash message
                messages.success(request, 'Te has registrado correctamente')

                login(request, user)

                return redirect('inicio')

        return render(request, 'registro.html',{
            'title': 'Registro',
            'register_form': register_form
            })

def user_login(request):

            # If the user is authenticated, redirect to the home page "inicio"
    if request.user.is_authenticated:
        return redirect('inicio')
    
    else:

        if request.method == 'POST':
            # I check that these two pieces of data are coming
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            # If authentication hasn't failed, it redirects us to the start/home page "inicio"
            if user is not None:
                login(request, user)
                return redirect('inicio')
            
            # If the user identifies themselves incorrectly, this message appears
            else:
                messages.warning(request, 'No te has identificado correctamente')

        return render(request, 'login.html', {
            'title': 'Identificate'
        })

def inicio(request):

    return render(request, 'inicio.html')

def logout_user(request):
    # I use the logout method and have it redirect me to the login URL
    logout(request)
    return redirect('login')