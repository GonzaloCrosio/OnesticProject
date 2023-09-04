from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from mainapp.form import RegisterForm

# Create your tests here.

# Test for registro in views.py
class RegistroViewTestCase(TestCase):

    def test_registro_view_authenticated_user(self):
        # Create an authenticated user
        User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Makes a GET request to the 'registration' view
        response = self.client.get(reverse('registro'))

        # Check that the response redirects to 'home'-'inicio' for an authenticated user
        self.assertRedirects(response, reverse('inicio'))

    def test_registro_view_invalid_post_data(self):
        # Invalid data for the registration form (passwords do not match)
        invalid_data = {
            'username': 'nuevo_usuario',
            'email': 'nuevo_usuario@example.com',
            'first_name': 'Nuevo',
            'last_name': 'Usuario',
            'password1': 'Password123',
            'password2': 'Password456',  # (passwords do not match)
        }

        # Makes a POST request with invalid data to register
        response = self.client.post(reverse('registro'), data=invalid_data)

        # Check the response stays on the same page ('registration') due to invalid data
        self.assertEqual(response.status_code, 200)

        # Check the user has not been created
        self.assertFalse(User.objects.filter(username='nuevo_usuario').exists())

    def test_registro_view_get_request(self):
        # Makes a GET request to the 'registration' view
        response = self.client.get(reverse('registro'))

        # Check the response has the 200 OK status code
        self.assertEqual(response.status_code, 200)

        # Check the registration form is present in the response
        self.assertIsInstance(response.context['register_form'], RegisterForm)

        # Check the title is as expected
        self.assertContains(response, '<title>Registro</title>')

# Test for login in views.py
class UserLoginTestCase(TestCase):
    def test_login_exitoso(self):
        # Create a test user
        user = User.objects.create_user(username='usuario_prueba', password='Password123')

        # Valid data for the login form
        datos_validos = {
            'username': 'usuario_prueba',
            'password': 'Password123',
        }

        # Makes a POST request with valid data to log in
        response = self.client.post(reverse('login'), data=datos_validos)

        # Check the response redirects to 'home'-'inicio'
        self.assertRedirects(response, reverse('inicio'))

        # Check the user is authenticated after logging in
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_fallido(self):
        # Invalid data for the login form.
        datos_invalidos = {
            'username': 'usuario_inexistente',
            'password': 'ContraseñaIncorrecta',
        }

        # Makes a POST request with invalid data to log in
        response = self.client.post(reverse('login'), data=datos_invalidos)

        # Check the page reloads with errors
        self.assertEqual(response.status_code, 200)

        # Check a warning message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'No te has identificado correctamente')

    def test_redireccion_usuario_autenticado(self):
        # Create a test user
        user = User.objects.create_user(username='usuario_prueba', password='Password123')

        # Log in as user_prueba
        self.client.login(username='usuario_prueba', password='Password123')

        # Makes a GET request to the login view while being authenticated
        response = self.client.get(reverse('login'))

        # Check the response redirects to 'home'-'inicio'
        self.assertRedirects(response, reverse('inicio'))

    def tearDown(self):
        # Clean up test data
        User.objects.filter(username='usuario_prueba').delete()