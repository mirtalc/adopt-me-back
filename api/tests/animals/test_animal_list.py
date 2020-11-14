import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.example_data import create_mock_animals
from api.tests.utils import mock_login, mock_authorization_header


class AnimalListTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'

    def setUp(self):
        create_mock_animals()
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

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
        response = self.client.get(url, **self.header)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))
