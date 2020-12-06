from rest_framework import serializers
from api.models import Animal
from api.serializers.adoptionstatus import AdoptionStatusSerializer
from api.serializers.vaccination import VaccinationBasicSerializer
from api.serializers.species import SpeciesSerializer


class AnimalSerializer(serializers.ModelSerializer):
    status = AdoptionStatusSerializer()
    species = SpeciesSerializer()

    class Meta:
        model = Animal
        fields = [
            'id',
            'name',
            'photo',
            'status',
            'species'
        ]


class AnimalPostPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = [
            'id',
            'name',
            'photo',
            'status',
            'species',
        ]


class AnimalDetailSerializer(serializers.ModelSerializer):
    status = AdoptionStatusSerializer()
    species = SpeciesSerializer()
    vaccinations = VaccinationBasicSerializer(many=True)

    class Meta:
        model = Animal
        fields = [
            'name',
            'photo',
            'species',
            'status',
            'vaccinations'
        ]
