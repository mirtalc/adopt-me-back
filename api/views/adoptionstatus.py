from rest_framework import viewsets
from rest_framework.response import Response

from api.models import AdoptionStatus
from api.serializers import AdoptionStatusStrictSerializer


class AdoptionStatusViewSet(viewsets.ViewSet):
    queryset = AdoptionStatus.objects.all()

    def list(self, request):
        serializer = AdoptionStatusStrictSerializer(
            self.queryset.all(), many=True)
        return Response(serializer.data)
