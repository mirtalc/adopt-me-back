from api.models import Animal
from api.tests.example_data import create_mock_animals
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
import json


class AnimalListTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'

    def setUp(self):
        create_mock_animals()

    def test_list_animals(self):
        expected_status = status.HTTP_200_OK
        expected_response = [
            {
                'id': 1,
                'name': 'Sudo',
                'status': 'ADOP'
            },
            {
                'id': 2,
                'name': 'Laika',
                'status': 'RIP'
            }
        ]

        url = self.animals_url
        response = self.client.get(url)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))
