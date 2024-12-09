from rest_framework.test import APITestCase
from django.contrib.auth.models import Group, User
from main.models import Zona

class ProtectedAPITests(APITestCase):
    def setUp(self):
        # Crear grupo Admin
        self.admin_group, _ = Group.objects.get_or_create(name='Admin')

        # Crear usuario normal
        self.user = User.objects.create_user(username='user', password='password123')
        
        # Crear usuario admin
        self.admin_user = User.objects.create_user(username='admin', password='password123')
        self.admin_user.groups.add(self.admin_group)

        # Crear datos de prueba
        self.zona1 = Zona.objects.create(nombre="Zona 1", codigo="brr")
        self.zona2 = Zona.objects.create(nombre="Zona 2", codigo="brr1")

    def test_api_access_and_data_retrieval_for_admin(self):
        # Login como admin
        self.client.login(username='admin', password='password123')

        # Hacer solicitud GET al endpoint
        response = self.client.get('/api/v1/zonas/')

        # Imprimir la respuesta en la terminal
        print(response.content)

        self.assertEqual(response.status_code, 200)

        expected_data = [
            {'id': self.zona1.id, 'nombre': self.zona1.nombre, 'codigo': self.zona1.codigo},
            {'id': self.zona2.id, 'nombre': self.zona2.nombre, 'codigo': self.zona2.codigo},
        ]
        self.assertEqual(response.json(), expected_data)
