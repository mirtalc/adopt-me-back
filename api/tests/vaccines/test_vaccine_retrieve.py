import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Vaccine
from api.tests.utils import mock_login, mock_authorization_header


class VaccineRetrieveTests(TestCase):
    client = APIClient()
    maxDiff = None
    vaccines_url = '/api/vaccines/'
    fixtures = ['initial_test_data.json']

    def setUp(self):
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_retrieve_vaccine(self):
        expected_status = status.HTTP_200_OK
        expected_response = {
            'id': 1,
            'name': 'Bordetella Bronchiseptica',
            'description': 'This highly infectious bacterium causes severe fits of coughing, whooping, vomiting, and, in rare cases, seizures and death. It is the primary cause of kennel cough.',
            'mandatory': True
        }

        url = f"{self.vaccines_url}1/"
        response = self.client.get(url)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_error_retrieve_inexistent_vaccine(self):
        expected_status = status.HTTP_404_NOT_FOUND
        expected_response = {
            'error_code': 'resource_not_found',
            'error_message': "Vaccine with id 999 was not found in our database"
        }

        url = f"{self.vaccines_url}999/"
        response = self.client.get(url)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))
