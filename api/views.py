from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse


def index(request):
    # example_data = {
    #     "Hello, world! You are at the api index"
    # }
    # example_status = status.HTTP_200_OK

    # return Response(example_data, status=example_status)
    return HttpResponse("Index view test, you are at the API!")
