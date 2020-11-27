import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.example_data import create_mock_animals, create_mock_vaccines
from api.tests.utils import mock_login, mock_authorization_header


class AnimalDestroyTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'

    def setUp(self):
        create_mock_animals()
        create_mock_vaccines()
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_delete_animal(self):
        expected_status = status.HTTP_204_NO_CONTENT

        url = f"{self.animals_url}1/"
        response = self.client.delete(url, **self.header)

        self.assertEqual(expected_status, response.status_code)

    def test_delete_animal_fails_inexistent_animal(self):
        expected_status = status.HTTP_404_NOT_FOUND
        expected_response = {
            'error_code': 'resource_not_found',
            'error_message': 'Animal with id 999 was not found in our database'
        }

        url = f"{self.animals_url}999/"
        response = self.client.delete(url, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_delete_animal_fails_no_token(self):
        expected_status = status.HTTP_401_UNAUTHORIZED
        expected_response = {
            'error_code': 'not_authenticated',
            'error_message': 'Authentication credentials were not provided.'
        }

        url = f"{self.animals_url}1/"
        response = self.client.delete(url)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)
