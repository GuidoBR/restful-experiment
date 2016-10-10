# -*- coding: UTF-8 -*- 
from django.db import models
from rest_framework_jwt.settings import api_settings

class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    phones = models.CharField(max_length=254)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    last_login = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=254)
    username = models.EmailField(max_length=254, default='default_user')

    def __str__(self):
        return "{} - {}".format(self.name, self.email)

    def save(self, *args, **kwargs):
        self.username = self.email

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(self)
        self.token = jwt_encode_handler(payload)
        super().save(*args, **kwargs)
