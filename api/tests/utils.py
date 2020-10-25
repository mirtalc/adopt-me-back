from rest_framework.test import APIClient
from django.contrib.auth.models import User


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
