from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Species
from api.serializers import SpeciesStrictSerializer


class SpeciesViewSet(viewsets.ViewSet):
    queryset = Species.objects.all()

    def list(self, request):
        serializer = SpeciesStrictSerializer(
            self.queryset.all(), many=True)
        return Response(serializer.data)
