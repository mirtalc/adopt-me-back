from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Vaccine
from api.serializers import VaccineSerializer
import api.exceptions.raisers as raiser


class VaccineViewSet(viewsets.ViewSet):
    queryset = Vaccine.objects.all()

    def list(self, request):
        serializer = VaccineSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            vaccine = self.queryset.get(pk=pk)
        except Vaccine.DoesNotExist:
            raiser.vaccine_not_found(vaccine_id=pk)

        serializer = VaccineSerializer(vaccine)
        return Response(serializer.data)
