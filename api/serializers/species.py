from rest_framework import serializers
from api.models import Species


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = [
            'uid',
            'name'
        ]


class SpeciesStrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'
