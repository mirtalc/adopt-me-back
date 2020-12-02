import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.utils import mock_login, mock_authorization_header


class AnimalListTests(TestCase):
    client = APIClient()
    maxDiff = None
    animals_url = '/api/animals/'
    fixtures = ['initial_test_data.json']

    def setUp(self):
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_list_animals(self):
        expected_status = status.HTTP_200_OK
        expected_response = [
            {
                'id': 1,
                'name': 'Sudo',
                'species': {'name': 'Dog', 'uid': 'DOG'},
                'status': {'name': 'Adopted', 'uid': 'ADOP'}
            },
            {
                'id': 2,
                'name': 'Laika',
                'species': {'name': 'Dog', 'uid': 'DOG'},
                'status': {'name': 'Deceased', 'uid': 'RIP'}
            },
            {
                'id': 3,
                'name': 'Mishi',
                'species': {'name': 'Cat', 'uid': 'CAT'},
                'status': {'name': 'Transferred', 'uid': 'TRANS'}
            }
        ]

        url = self.animals_url
        response = self.client.get(url, **self.header)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))
