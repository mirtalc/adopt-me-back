from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from api.models import Animal
from api.serializers import AnimalSerializer, AnimalDetailSerializer
from api.utils.helpers import has_body_params
import api.exceptions.raisers as raiser


class AnimalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Animal.objects.all()

    def list(self, request):
        serializer = AnimalSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            animal = self.queryset.get(pk=pk)
        except Animal.DoesNotExist:
            raiser.animal_not_found(animal_id=pk)

        serializer = AnimalDetailSerializer(animal)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AnimalSerializer(data=request.data, many=False)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        try:
            animal = self.queryset.get(pk=pk)
        except Animal.DoesNotExist:
            raiser.animal_not_found(animal_id=pk)

        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):
        try:
            animal = self.queryset.get(pk=pk)

            if(not has_body_params(request)):
                raiser.no_values_supplied()

            serializer = AnimalSerializer(instance=animal,
                                          data=request.data,
                                          partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        except Animal.DoesNotExist:
            raiser.animal_not_found(animal_id=pk)
        except ValidationError:
            raiser.invalid_fields(serializer.errors)
