import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from adoptme.settings import BASE_DIR
from api.tests.utils import mock_login, mock_authorization_header, add_headers_for_file
from api.models import Animal


class AnimalPatchPhotoTests(TestCase):
    maxDiff = None
    animals_url = '/api/animals/'
    photo_suffix = 'profilepic/'
    fixtures = ['initial_test_data.json']
    example_picture = f'{BASE_DIR}/api/tests/example_pic.jpg'

    def setUp(self):
        self.client = APIClient()
        access_token = mock_login().get('access')
        self.header = mock_authorization_header(access_token)

    def test_patch_photo(self):
        expected_status = status.HTTP_200_OK
        body_params = {
            'file': open(self.example_picture, 'br'),
        }

        headers = add_headers_for_file(self.header)
        url = f"{self.animals_url}1/{self.photo_suffix}"
        response = self.client.patch(url, body_params, **headers)

        animal = Animal.objects.get(pk=1)

        self.assertIn('example_pic', str(animal.photo))
        self.assertEqual(expected_status, response.status_code)

    def test_patch_photo_fails_no_attached_file(self):
        expected_status = status.HTTP_400_BAD_REQUEST
        expected_response = {
            'error_code': 'parse_error',
            'error_message': 'Attachment file missing required for this action'
        }

        url = f"{self.animals_url}1/{self.photo_suffix}"
        response = self.client.patch(url, **self.header)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_patch_photo_fails_inexistent_animal(self):
        expected_status = status.HTTP_404_NOT_FOUND
        expected_response = {
            'error_code': 'resource_not_found',
            'error_message': 'Animal with id 999 was not found in our database'
        }
        body_params = {
            'file': open(self.example_picture, 'br'),
        }

        headers = add_headers_for_file(self.header)
        url = f"{self.animals_url}999/{self.photo_suffix}"
        response = self.client.patch(url, body_params, **headers)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)

    def test_patch_photo_fails_no_token(self):
        expected_status = status.HTTP_401_UNAUTHORIZED
        expected_response = {
            'error_code': 'not_authenticated',
            'error_message': 'Authentication credentials were not provided.'
        }

        url = f"{self.animals_url}1/{self.photo_suffix}"
        response = self.client.patch(url)

        self.assertEqual(expected_response, json.loads(response.content))
        self.assertEqual(expected_status, response.status_code)
