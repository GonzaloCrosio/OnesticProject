from django.shortcuts import render, redirect
from django.contrib import messages
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

        # Si el usuario está identificado que nos rediriga a inicio
    if request.user.is_authenticated:
        return redirect('inicio')
    
    else:
        register_form = RegisterForm()

        # Para guardar un usuario nuevo a través del formulario creado en register. Si el formulario es válido que me guarde el usuario.
        # El método form está armado para que me guarde el usuario directamente en django. Si el usuario es creado te redirige a la página de inicio
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                # Creación del mensaje flash
                messages.success(request, 'Te has registrado correctamente')

                return redirect('/inicio')

        return render(request, 'registro.html',{
            'title': 'Registro',
            'register_form': register_form
            })

def user_login(request):

            # Si el usuario está identificado que nos rediriga a inicio
    if request.user.is_authenticated:
        return redirect('inicio')
    
    else:

        if request.method == 'POST':
            # Verifico que me esté llegando estos dos datos
            username = request.POST.get('username')
            password = request.POST.get('password')

            # A la variable user le paso los datos que tiene el usuario.
            user = authenticate(request, username=username, password=password)

            # Si la autenticación no ha fallado nos redirige al inicio
            if user is not None:
                login(request, user)
                return redirect('inicio')
            
            # Si el usuario se identifica de forma errónea nos aparece este mensaje
            else:
                messages.warning(request, 'No te has identificado correctamente')

        return render(request, 'login.html', {
            'title': 'Identificate'
        })

def inicio(request):

    return render(request, 'inicio.html')

def logout_user(request):
    # Utilizo el método logout y que me redireccione a la url de login
    logout(request)
    return redirect('login')