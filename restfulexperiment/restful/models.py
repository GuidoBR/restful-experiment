# -*- coding: UTF-8 -*- 
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    phones = models.CharField(max_length=254)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    last_login = models.CharField(max_length=254)
    token = models.CharField(max_length=254)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)
