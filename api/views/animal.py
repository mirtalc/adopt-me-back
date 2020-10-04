from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse
from api.models import Animal, Vaccine
from api.serializers import AnimalSerializer, AnimalDetailSerializer


class AnimalViewSet(viewsets.ViewSet):
    queryset = Animal.objects.all()

    def list(self, request):
        serializer = AnimalSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        animal = get_object_or_404(self.queryset, pk=pk)
        serializer = AnimalDetailSerializer(animal)
        return Response(serializer.data)
