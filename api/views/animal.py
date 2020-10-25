from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Animal
from api.serializers import AnimalSerializer, AnimalDetailSerializer
import api.exceptions.raisers as raiser
from rest_framework.permissions import IsAuthenticated


class AnimalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Animal.objects.all()

    def list(self, request):
        serializer = AnimalSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            animal = self.queryset.get(pk=pk)
        except Animal.DoesNotExist:
            raiser.animal_not_found(animal_id=pk)

        serializer = AnimalDetailSerializer(animal)
        return Response(serializer.data)
