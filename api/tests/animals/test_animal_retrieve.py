from api.models import Animal, Vaccine, Vaccination
from api.tests.example_data import create_mock_animals, create_mock_vaccines
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
import json


class AnimalRetrieveTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'

    def setUp(self):
        create_mock_animals()
        create_mock_vaccines()

    def test_retrieve_animal_without_vaccines(self):
        expected_status = status.HTTP_200_OK
        expected_response = {
            'name': 'Sudo',
            'status': 'ADOP',
            'vaccinations': []
        }

        url = f"{self.animals_url}1/"
        response = self.client.get(url)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))

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
        response = self.client.get(url)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))
