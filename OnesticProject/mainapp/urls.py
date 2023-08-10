from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.servicios, name="servicios"),
    path('empleos/', views.empleos, name="empleos"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/', views.contacto, name="contacto"),
]