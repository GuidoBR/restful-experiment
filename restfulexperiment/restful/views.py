# -*- coding: UTF-8 -*-
from django.shortcuts import render
from rest_framework import authentication, viewsets
from restfulexperiment.restful.models import User
from restfulexperiment.restful.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
