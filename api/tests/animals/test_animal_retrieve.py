import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Animal, Vaccine, Vaccination
from api.tests.utils import mock_login, mock_authorization_header


class AnimalRetrieveTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'
    fixtures = ['initial_test_data.json']

    def setUp(self):
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_retrieve_animal_without_vaccines(self):
        expected_status = status.HTTP_200_OK
        expected_response = {
            'name': 'Laika',
            'species': {'name': 'Dog', 'uid': 'DOG'},
            'status': {'name': 'Deceased', 'uid': 'RIP'},
            'vaccinations': []
        }

        url = f"{self.animals_url}2/"
        response = self.client.get(url, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_retrieve_animal_with_vaccines(self):
        expected_status = status.HTTP_200_OK
        expected_response = {
            'name': 'Sudo',
            'species': {'name': 'Dog', 'uid': 'DOG'},
            'status': {'name': 'Adopted', 'uid': 'ADOP'},
            'vaccinations': [
                {
                    'date_vaccinated': '2016-10-23',
                    'incidences': 'Dog was very scared but the process went well.',
                    'vaccine': {
                        'mandatory': True,
                        'name': 'Bordetella Bronchiseptica'
                    }
                },
                {
                    'date_vaccinated': '2020-10-09',
                    'incidences': 'Vaccine caused a small reaction',
                    'vaccine': {
                        'mandatory': False,
                        'name': 'Canine Distemper'
                    }
                }
            ]
        }

        url = f"{self.animals_url}1/"
        response = self.client.get(url, **self.header)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))

    def test_error_retrieve_inexistent_animal(self):
        expected_status = status.HTTP_404_NOT_FOUND
        expected_response = {
            'error_code': 'resource_not_found',
            'error_message': "Animal with id 999 was not found in our database"
        }

        url = f"{self.animals_url}999/"
        response = self.client.get(url, **self.header)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))
