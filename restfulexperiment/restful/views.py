# -*- coding: UTF-8 -*-
from django.shortcuts import render
from rest_framework import authentication, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from restfulexperiment.restful.models import User
from restfulexperiment.restful.serializers import UserSerializer


@api_view(['GET'])
@permission_classes((AllowAny, ))
def user_collection(request):
    if request.method == 'GET':
        users = User.objects.all().order_by('-created')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def user_element(request, pk=None):
    if request.method == 'GET':
        try:
                user = User.objects.get(pk=pk)
        except User.DoesNotExist:
                return Response(status=404)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'POST':
        data = {
                "name": request.data.get('name'),
                "email": request.data.get('email'),
                "password": request.data.get('password'),
                "phones": request.data.get('phones'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

