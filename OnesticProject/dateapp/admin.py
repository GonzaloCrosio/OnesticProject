from django.contrib import admin

# import the two model-classes that I created in the models.py.
from .models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):                # Show read-only fields within the admin user
    readonly_fields = ('created_at' , 'update_at')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'update_at')

admin.site.register(Category, CategoryAdmin)         # Create the Category section in the admin user
admin.site.register(Product, ProductAdmin)           # Create the Product section in the admin user
