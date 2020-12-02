from rest_framework import serializers
from api.models import AdoptionStatus


class AdoptionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionStatus
        fields = [
            'uid',
            'name'
        ]


class AdoptionStatusStrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionStatus
        fields = '__all__'
