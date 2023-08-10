from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Category

# Create your views here.

def datos(request):
    productos = Product.objects.all()
    return render(request, 'datos.html', {'productos': productos})

# For delete items in table SQL:
def delete_product(request, id):
    if request.method == 'POST':
    # First identify article and then delete it
        producto = Product.objects.get(id=id)
        producto.delete()
        # After delete let go to datos page
        return redirect('datos')
    
# For created products
def save(request):
    if request.method == 'POST':
        title = request.POST['title']
        if len(title) <= 5:
            return HttpResponse('El nombre es muy pequeño')
        content = request.POST['content']
        public = request.POST['public']
        category_ids = request.POST.getlist('categories')       # Gets a list of selected IDs

        # Get the objects of the selected categories
        selected_categories = Category.objects.filter(id__in=category_ids)

        productos = Product(
            title=title,
            content=content,
            public=public,
        )

        productos.save()

        productos.categories.set(selected_categories)

        return redirect('datos')

    return render(request, 'crear_datos.html')  # Render the form in case of GET request