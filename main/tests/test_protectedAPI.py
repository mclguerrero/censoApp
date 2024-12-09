from rest_framework.test import APITestCase
from django.contrib.auth.models import Group, User

class ProtectedAPITests(APITestCase):
    def setUp(self):
        self.admin_group, _ = Group.objects.get_or_create(name='Admin')

        self.user = User.objects.create_user(username='user', password='password123')
        
        self.admin_user = User.objects.create_user(username='admin', password='password123')
        self.admin_user.groups.add(self.admin_group)

    def test_swagger_access_for_admin(self):
        self.client.login(username='admin', password='password123')

        response = self.client.get('/swagger/')
        self.assertEqual(response.status_code, 200)  # Admin debería acceder

    def test_swagger_access_for_non_admin(self):
        self.client.login(username='user', password='password123')

        response = self.client.get('/swagger/')
        self.assertEqual(response.status_code, 403)  # Usuario normal debería ser denegado

    def test_api_access_for_admin(self):
        self.client.login(username='admin', password='password123')

        response = self.client.get('/api/v1/zonas/')
        self.assertEqual(response.status_code, 200)  # Admin debería acceder

    def test_api_access_for_non_admin(self):
        self.client.login(username='user', password='password123')

        response = self.client.get('/api/v1/zonas/')
        self.assertEqual(response.status_code, 403)  # Usuario normal debería ser denegado
