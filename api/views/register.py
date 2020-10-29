from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from api.serializers import RegistrationSerializer


class RegisterViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = make_password(self.request.data['password'])
        serializer.save(password=password)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
