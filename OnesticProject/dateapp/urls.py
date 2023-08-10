from django.urls import path
from . import views

urlpatterns = [
    path('datos/', views.datos, name="datos"),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('crear_datos/', views.save, name="save"),
]