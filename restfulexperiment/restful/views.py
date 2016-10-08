# -*- coding: UTF-8 -*-
from django.shortcuts import render
from rest_framework import authentication, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restfulexperiment.restful.models import User
from restfulexperiment.restful.serializers import UserSerializer


@api_view(['GET'])
def user_collection(request):
    if request.method == 'GET':
        users = User.objects.all().order_by('-created')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user_element(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
