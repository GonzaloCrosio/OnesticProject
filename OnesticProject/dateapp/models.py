from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=110)                         
    description = models.CharField(max_length=250)                  
    created_at = models.DateField()                                 
    update_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Categoría"                                  # It is used to change the name of the list in the administrator user
        verbose_name_plural = "Categorías"                          
        ordering = ['id']                                           


    def __str__(self):                                              # It is used for the name of the category to appear in the list of the administrator user
        return f"{self.name}"

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título") 
    content = models.TextField(verbose_name="Contenido")            
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='products') 
    public = models.BooleanField(verbose_name="¿Publicado?")         
    user = models.ForeignKey(User, verbose_name='Usuario', editable=False, on_delete=models.CASCADE, default=1)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)             
    update_at = models.DateTimeField(auto_now=True)                  

    class Meta:
        verbose_name = "Producto"                                   # It is used to change the name of the list in the administrator user
        verbose_name_plural = "Productos"                           # It is used to change the plural name of the list in the administrator user
        ordering = ['id']                                           # Order the list on the admin user

    def __str__(self):                                              # It is used for the name of the product to appear in the list of the administrator user
        public_status = "publicado" if self.public else "privado"
        return f"{self.title} ({public_status})"
