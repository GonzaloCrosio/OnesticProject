from django.test import TestCase
from django.urls import reverse
from dateapp.models import Product, Category
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.

# Test for Category in models.py
class CategoryModelTestCase(TestCase):
    def test_create_category(self):
        # Create a test category.
        category = Category.objects.create(
            name='Categoría de prueba',
            description='Descripción de prueba',
            created_at=timezone.now()
        )

        # Check the category has been saved correctly in the database
        self.assertEqual(Category.objects.count(), 1)

        # Retrieve the category from the database and verify its attributes
        saved_category = Category.objects.get(id=category.id)
        self.assertEqual(saved_category.name, 'Categoría de prueba')
        self.assertEqual(saved_category.description, 'Descripción de prueba')
        self.assertIsNotNone(saved_category.created_at)
        self.assertIsNotNone(saved_category.update_at)

    def test_category_str_method(self):
        # Create a test category.
        category = Category.objects.create(
            name='Categoría de prueba',
            description='Descripción de prueba',
            created_at=timezone.now()
        )

        # Check the __str__ method returns the category name
        self.assertEqual(str(category), 'Categoría de prueba')

# Test for Product in models.py
class ProductModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test category
        self.category = Category.objects.create(
            name='Categoría de prueba',
            description='Descripción de prueba',
            created_at=timezone.now()
        )

    def tearDown(self):
        # Delete the test user
        self.user.delete()

    def test_create_product(self):
        # Create a test product.
        product = Product.objects.create(
            title='Producto de prueba',
            content='Contenido de prueba',
            public=True,
            user=self.user,
        )

        # Associate the product with the test category
        product.categories.add(self.category)

        # Check the product has been successfully saved in the database
        self.assertEqual(Product.objects.count(), 1)

        # Retrieve the product from the database and verify its attributes
        saved_product = Product.objects.get(id=product.id)
        self.assertEqual(saved_product.title, 'Producto de prueba')
        self.assertEqual(saved_product.content, 'Contenido de prueba')
        self.assertTrue(saved_product.public)
        self.assertEqual(saved_product.user, self.user)
        self.assertEqual(list(saved_product.categories.all()), [self.category])

    def test_product_str_method(self):
        # Create a test product
        product = Product.objects.create(
            title='Producto de prueba',
            content='Contenido de prueba',
            public=True,
            user=self.user,
        )

        # Check the __str__ method returns the product's name and publication status.
        self.assertEqual(str(product), 'Producto de prueba (publicado)')


# Test de datos in views.py
class DatosViewTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def tearDown(self):
        # Delete the test user
        self.user.delete()

    def test_datos_view_returns_correct_template(self):
        # Use the user created in setUp
        user = self.user

        # Create some test products
        Product.objects.create(title='Producto 1', content='Contenido 1', public=True, user=user)
        Product.objects.create(title='Producto 2', content='Contenido 2', public=True, user=user)

        response = self.client.get(reverse('datos'))
        
        # Check the view returns the correct status code (200 OK)
        self.assertEqual(response.status_code, 200)
        
        # Ensure that the 'datos.html' template is being used
        self.assertTemplateUsed(response, 'datos.html')
        
        # Confirm that the products are displayed in the response
        self.assertContains(response, 'Producto 1')
        self.assertContains(response, 'Producto 2')

# Test for delete_product in views.py
class DeleteProductViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def tearDown(self):
        # Delete the test user
        self.user.delete()

    def test_delete_product(self):
        # Use the user created in setUp
        user = self.user

        # Create a test product
        producto = Product.objects.create(title='Producto de prueba', content='Contenido de prueba', public=True, user=user)

        # Make a POST request to delete the product
        response = self.client.post(reverse('delete_product', args=[producto.id]))

        # Check the status code is a redirection (302)
        self.assertEqual(response.status_code, 302)

        # Check the product no longer exists in the database
        self.assertFalse(Product.objects.filter(id=producto.id).exists())

        # Confirm that the redirection is to the 'datos' view
        self.assertRedirects(response, reverse('datos'))

# Test for save in views.py
class SaveViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def tearDown(self):
        # Delete the test user
        self.user.delete()

    def test_save_product_valid_data(self):
        # Use the user created in setUp
        user = self.user

    def test_save_product_valid_data(self):
        # Create some test categories
        category1 = Category.objects.create(name='Categoría 1', created_at=timezone.now())
        category2 = Category.objects.create(name='Categoría 2', created_at=timezone.now())

        # Test data for the POST request
        post_data = {
            'title': 'Producto de prueba',
            'content': 'Contenido de prueba',
            'public': True,
            'categories': [category1.id, category2.id],
        }

        # Make a POST request to save the product
        response = self.client.post(reverse('save'), data=post_data)

        # Check the status code is a redirection (302)
        self.assertEqual(response.status_code, 302)

        # Check the product has been saved in the database
        self.assertTrue(Product.objects.filter(title='Producto de prueba').exists())

        # Check the categories are associated with the product
        product = Product.objects.get(title='Producto de prueba')
        self.assertEqual(list(product.categories.all()), [category1, category2])

        # Check the redirection is to the 'datos' view
        self.assertRedirects(response, reverse('datos'))

    def test_save_product_invalid_data(self):
        # Test data for the POST request with a too short title
        post_data = {
            'title': 'Short',
            'content': 'Contenido de prueba',
            'public': True,
            'categories': [],
        }

        # Make a POST request to save the product with invalid data
        response = self.client.post(reverse('save'), data=post_data)

        # Check the status code is 200 (invalid form)
        self.assertEqual(response.status_code, 200)

        # Check the error message is present in the response
        self.assertContains(response, 'El nombre es muy pequeño')

        # Check the product has not been saved in the database
        self.assertFalse(Product.objects.filter(title='Short').exists())


