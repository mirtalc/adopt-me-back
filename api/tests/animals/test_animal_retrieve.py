import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Animal, Vaccine, Vaccination
from api.tests.example_data import create_mock_animals, create_mock_vaccines
from api.tests.utils import mock_login, mock_authorization_header


class AnimalRetrieveTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'

    def setUp(self):
        create_mock_animals()
        create_mock_vaccines()
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_retrieve_animal_without_vaccines(self):
        expected_status = status.HTTP_200_OK
        expected_response = {
            'name': 'Sudo',
            'status': 'ADOP',
            'vaccinations': []
        }

        url = f"{self.animals_url}1/"
        response = self.client.get(url, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_retrieve_animal_with_vaccines(self):
        expected_status = status.HTTP_200_OK
        expected_response = {
            'name': 'Sudo',
            'status': 'ADOP',
            'vaccinations': [
                {
                    'date_vaccinated': '2016-09-27',
                    'incidences': 'Dog was initially scared',
                    'vaccine': 2
                }
            ]
        }

        # Simulate that animal has been vaccinated
        my_animal = Animal.objects.get(pk=1)
        some_vaccine = Vaccine.objects.get(pk=2)
        Vaccination.objects.create(
            animal=my_animal,
            vaccine=some_vaccine,
            date_vaccinated='2016-09-27',
            incidences='Dog was initially scared'
        )

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
