# -*- coding: UTF-8 -*-
from django.shortcuts import render
from rest_framework import authentication, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
    if request.method == 'GET':
        try:
                user = User.objects.get(pk=pk)
        except User.DoesNotExist:
                return Response(status=404)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'POST':
        data = {
                "name": request.DATA.get('name'),
                "email": request.DATA.get('email'),
                "password": request.DATA.get('password'),
                "phones": request.DATA.get('phones'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

