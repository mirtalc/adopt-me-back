from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Animal, Vaccine, Vaccination, AdoptionStatus, Species


class StatusUidSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionStatus
        fields = [
            'name',
            'uid'
        ]


class VaccinationBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = [
            'date_vaccinated',
            'incidences',
            'vaccine'
        ]


class AnimalSerializer(serializers.ModelSerializer):
    status = StatusUidSerializer()

    class Meta:
        model = Animal
        fields = [
            'id',
            'name',
            'status'
        ]


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = [
            'id',
            'name',
            'description',
            'mandatory'
        ]


class AnimalDetailSerializer(serializers.ModelSerializer):
    vaccinations = VaccinationBasicSerializer(many=True)

    class Meta:
        model = Animal
        fields = [
            'name',
            'status',
            'vaccinations'
        ]


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
