from rest_framework.test import APITestCase
from rest_framework import status
from .models import Build


class BuildAPITest(APITestCase):
    def test_get_build_objects(self):
        response = self.client.get('/build/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_build_object_details(self):
        id = 1
        response = self.client.get(f'/build/{id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], id)
