from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.servicios, name="servicios"),
    path('empleos/', views.empleos, name="empleos"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/', views.contacto, name="contacto"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.user_login, name="login"),
    path('inicio/', views.inicio, name="inicio"),
    path('logout/', views.logout_user, name="logout"),
]