from rest_framework import serializers
from api.models import Animal, Vaccine, Vaccination


class VaccinationBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = [
            'date_vaccinated',
            'incidences',
            'vaccine'
        ]


class AnimalSerializer(serializers.ModelSerializer):
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
