import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.tests.utils import mock_login, mock_authorization_header


class AdoptionStatusListTests(TestCase):
    client = APIClient()
    maxDiff = None
    status_url = '/api/adoption-statuses/'
    fixtures = ['initial_test_data.json']

    def setUp(self):
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_list_adoption_statuses(self):
        expected_status = status.HTTP_200_OK
        expected_response = [
            {
                'id': 1,
                'uid': 'PROC',
                'name': 'Processing',
                'description': 'Processing or recovering; cannot yet be adopted'
            },
            {
                'id': 2,
                'uid': 'AVAIL',
                'name': 'Available',
                'description': 'Available for adopting'
            },
            {
                'id': 3,
                'uid': 'ADOP',
                'name': 'Adopted',
                'description': 'Already adopted. Yay!'
            },
            {
                'id': 4,
                'uid': 'TRANS',
                'name': 'Transferred',
                'description': 'Transferred to another shelter'
            },
            {
                'id': 5,
                'uid': 'RIP',
                'name': 'Deceased',
                'description': 'Unfortunately, it died'
            }
        ]

        url = self.status_url
        response = self.client.get(url, **self.header)

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_response, json.loads(response.content))
