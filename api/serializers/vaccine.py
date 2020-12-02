from rest_framework import serializers
from api.models import Vaccine


class VaccineBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = [
            'name',
            'mandatory'
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
