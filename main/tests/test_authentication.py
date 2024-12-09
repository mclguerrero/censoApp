from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

class UserTests(TestCase):

    def setUp(self):
        # Crear el grupo 'Admin' y 'Usuario' para las pruebas
        self.admin_group, created = Group.objects.get_or_create(name='Admin')
        self.usuario_group, created = Group.objects.get_or_create(name='Usuario')

        # Definir la URL de signup
        self.signup_url = reverse('signup')
        self.signin_url = reverse('signin')  
        self.user_data = {
            'username': 'newWuser',  
            'password1': 'password123123',
            'password2': 'password123123'
        }

    def test_user_signup_and_group_assignment(self):
        # Registrar el usuario
        response = self.client.post(self.signup_url, self.user_data)

        # Verificar que la respuesta sea un redireccionamiento (302)
        print(response.status_code) 
        self.assertEqual(response.status_code, 302, "Expected a redirect, but got a different response.")

        # Verificar que se redirige a la página de inicio de sesión
        self.assertRedirects(response, self.signin_url)

        # Obtener el usuario recién creado (usando el nombre correcto)
        user = get_user_model().objects.get(username='newWuser')  # Cambiar 'new_user' por 'newWuser'

        # Verificar que el usuario tiene el grupo 'Usuario' asignado por defecto
        self.assertTrue(user.groups.filter(name='Usuario').exists())

        # Cambiar el grupo del usuario a 'Admin'
        user.groups.clear() 
        user.groups.add(self.admin_group)  
        user.save()

        # Verificar que el usuario ahora tiene el grupo 'Admin'
        self.assertTrue(user.groups.filter(name='Admin').exists())
        self.assertEqual(user.groups.count(), 1) 

        # Realizar el login a través de la vista de inicio de sesión
        login_data = {
            'username': 'newWuser',
            'password': 'password123123'
        }
        login_response = self.client.post(self.signin_url, login_data)

        self.assertEqual(login_response.status_code, 302)  
        self.assertRedirects(login_response, reverse('listar_eventos')) 