import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.utils import mock_login, mock_authorization_header


class AnimalCreateTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'
    fixtures = ['initial_test_data.json']

    def setUp(self):
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_create_basic_animal(self):
        expected_status = status.HTTP_201_CREATED
        expected_response = {
            'id': 6,
            'name': 'Kittie',
            'species': 1,
            'status': 2
        }
        body_params = {
            'name': 'Kittie',
            'species': 1,
            'status': 2,
        }

        url = f"{self.animals_url}"
        self.client.post(url, **self.header)
        self.client.post(url, **self.header)
        response = self.client.post(url, body_params, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_create_fails_invalid_status(self):
        expected_status = status.HTTP_400_BAD_REQUEST
        expected_response = {
            'status': ['Invalid pk "99" - object does not exist.']
        }
        body_params = {
            'name': 'Kittie',
            'status': 99,
        }

        url = f"{self.animals_url}"
        self.client.post(url, **self.header)
        self.client.post(url, **self.header)
        response = self.client.post(url, body_params, **self.header)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))

    def test_create_fails_no_token(self):
        expected_status = status.HTTP_401_UNAUTHORIZED
        expected_response = {
            'error_code': 'not_authenticated',
            'error_message': "Authentication credentials were not provided."
        }

        url = f"{self.animals_url}"
        response = self.client.post(url)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))

    def test_create_animal_with_vaccines(self):
        pass  # //TODO
