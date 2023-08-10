from django.shortcuts import render

# Create your views here.

def servicios(request):

    return render(request, 'servicios.html')

def empleos(request):

    return render(request, 'empleos.html')

def nosotros(request):

    return render(request, 'nosotros.html')

def contacto(request):

    return render(request, 'contacto.html')