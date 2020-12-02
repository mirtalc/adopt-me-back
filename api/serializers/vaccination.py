from rest_framework import serializers
from api.models import Vaccination
from api.serializers.vaccine import VaccineBasicSerializer


class VaccinationBasicSerializer(serializers.ModelSerializer):
    vaccine = VaccineBasicSerializer()

    class Meta:
        model = Vaccination
        fields = [
            'date_vaccinated',
            'incidences',
            'vaccine'
        ]
