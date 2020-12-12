import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.utils import mock_login, mock_authorization_header


class SpeciesListTests(TestCase):
    client = APIClient()
    maxDiff = None
    status_url = '/api/species/'
    fixtures = ['initial_test_data.json']

    def setUp(self):
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_list_species(self):
        expected_status = status.HTTP_200_OK
        expected_response = [
            {
                'id': 1,
                'uid': 'CAT',
                'name': 'Cat',
                'fullname': 'Felis catus'
            },
            {
                'id': 2,
                'uid': 'DOG',
                'name': 'Dog',
                'fullname': 'Canis lupus familiaris'
            }
        ]

        url = self.status_url
        response = self.client.get(url, **self.header)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))
