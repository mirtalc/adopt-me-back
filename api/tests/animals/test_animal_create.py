import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.example_data import create_mock_vaccines
from api.tests.utils import mock_login, mock_authorization_header


class AnimalRetrieveTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'

    def setUp(self):
        create_mock_vaccines()
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_create_default_animal(self):
        expected_status = status.HTTP_201_CREATED
        expected_response = {
            'id': 4,
            'name': 'Mistery',
            'status': 'PROC',
        }

        url = f"{self.animals_url}"
        response = self.client.post(url, **self.header)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))

    def test_create_basic_animal(self):
        expected_status = status.HTTP_201_CREATED
        expected_response = {
            'id': 3,
            'name': 'Kittie',
            'status': 'TRANS',
        }
        body_params = {
            'name': 'Kittie',
            'status': 'TRANS',
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
