from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=3,
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
        ]

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
