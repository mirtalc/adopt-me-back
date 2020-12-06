from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.models import Animal, Vaccine


def mock_login(username='test_user', password='test_password', is_superuser=False):
    mock_user = User.objects.create(username=username, is_superuser=False)
    mock_user.set_password(password)
    mock_user.save()

    body_params = {
        "username": username,
        "password": password
    }

    client = APIClient()
    response = client.post('/api/token/', body_params)

    return response.data


def mock_authorization_header(access_token=None):
    return {
        "HTTP_AUTHORIZATION": f"Bearer {access_token}",
    }


def get_mock_animal(animal_id, name, status, vaccinations=[]):
    animal, animal_created = Animal.objects.get_or_create(pk=animal_id)
    animal.name = name
    animal.status = status
    animal.vaccinations.set(vaccinations)
    animal.save()

    return animal


def get_mock_vaccine(vaccine_id, name, description='', mandatory=False):
    vaccine, vaccine_created = Vaccine.objects.get_or_create(pk=vaccine_id)
    vaccine.name = name
    vaccine.description = description
    vaccine.mandatory = mandatory
    vaccine.save()

    return vaccine


def add_headers_for_file(headers, name='file', filename='example_pic.jpg'):
    headers['Content-Type'] = 'image/jpeg'
    headers['Content-Disposition'] = f'attachment; name="{name}"; filename="{filename}"'
    return headers
