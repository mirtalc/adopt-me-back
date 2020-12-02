import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.utils import mock_login, mock_authorization_header


class AnimalPartialUpdateTests(TestCase):
    maxDiff = None
    animals_url = '/api/animals/'
    fixtures = ['initial_test_data.json']

    def setUp(self):
        self.client = APIClient()
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_patch_animal(self):
        expected_status = status.HTTP_200_OK
        expected_response = {
            'id': 1,
            'name': "A different name",
            'species': 2,
            'status': 3
        }
        expected_response_2 = {
            'id': 1,
            'name': "A different name",
            'species': 2,
            'status': 4
        }
        body_params = {
            'name': "A different name",
        }
        body_params_2 = {
            'status': 4
        }

        url = f"{self.animals_url}1/"
        response = self.client.patch(url, body_params, **self.header)
        response_2 = self.client.patch(url, body_params_2, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_response_2, json.loads(response_2.content))
        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_status, response_2.status_code)

    def test_patch_animal_invalid_value(self):
        expected_status = status.HTTP_400_BAD_REQUEST
        expected_response = {
            'error_code': 'invalid_fields',
            'error_message':
                'Invalid field values found: \n'
                'Errors with field >status<\n'
                '>> Invalid pk "99" - object does not exist.\n'
        }
        body_params = {
            'status': 99
        }

        url = f"{self.animals_url}1/"
        response = self.client.patch(
            url, body_params, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
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
