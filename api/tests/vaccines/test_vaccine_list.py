import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Vaccine
from api.tests.utils import mock_login, mock_authorization_header


class VaccineListTests(TestCase):
    client = APIClient()
    maxDiff = None
    vaccines_url = '/api/vaccines/'
    fixtures = ['initial_test_data.json']

    def setUp(self):
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_list_vaccines(self):
        expected_status = status.HTTP_200_OK
        expected_response = [
            {
                'id': 1,
                'name': 'Bordetella Bronchiseptica',
                'description': 'This highly infectious bacterium causes severe fits of coughing, whooping, vomiting, and, in rare cases, seizures and death. It is the primary cause of kennel cough.',
                'mandatory': True
            },
            {
                'id': 2,
                'name': 'Canine Distemper',
                'description': 'A severe and contagious disease caused by a virus that attacks the respiratory, gastrointestinal (GI), and nervous systems of dogs.',
                'mandatory': False
            },
            {
                'id': 3,
                'name': 'Canine Hepatitis',
                'description': 'Infectious canine hepatitis is a highly contagious viral infection that affects the liver, kidneys, spleen, lungs, and the eyes of the affected dog.',
                'mandatory': False
            }
        ]

        url = self.vaccines_url
        response = self.client.get(url)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)
