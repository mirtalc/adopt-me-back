import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.example_data import create_mock_animals, create_mock_vaccines
from api.tests.utils import mock_login, mock_authorization_header


class AnimalRetrieveTests(TestCase):
    maxDiff = None
    animals_url = '/api/animals/'

    def setUp(self):
        self.client = APIClient()
        create_mock_animals()
        create_mock_vaccines()
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_patch_animal(self):
        expected_status = status.HTTP_200_OK
        expected_response = {
            'id': 1,
            'name': "A different name",
            'status': 'ADOP'
        }
        body_params = {
            'name': "A different name"
        }

        url = f"{self.animals_url}1/"
        response = self.client.patch(url, body_params, ** self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_patch_animal_invalid_value(self):
        expected_status = status.HTTP_400_BAD_REQUEST
        body_params = {
            'name': True,
            'status': 'INVENT'
        }

        url = f"{self.animals_url}1/"
        response = self.client.patch(
            url, body_params, **self.header)

        self.assertEqual(expected_status, response.status_code)

    def test_patch_animal_fails_no_values(self):
        expected_status = status.HTTP_400_BAD_REQUEST
        expected_response = {
            'error_code': 'no_values_supplied',
            'error_message': 'You did not supplied any values to update'
        }

        url = f"{self.animals_url}1/"
        response = self.client.patch(url, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_patch_animal_fails_inexistent_animal(self):
        expected_status = status.HTTP_404_NOT_FOUND
        expected_response = {
            'error_code': 'resource_not_found',
            'error_message': 'Animal with id 999 was not found in our database'
        }

        url = f"{self.animals_url}999/"
        response = self.client.patch(url, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_delete_animal_fails_no_token(self):
        expected_status = status.HTTP_401_UNAUTHORIZED
        expected_response = {
            'error_code': 'not_authenticated',
            'error_message': 'Authentication credentials were not provided.'
        }

        url = f"{self.animals_url}1/"
        response = self.client.patch(url)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)
