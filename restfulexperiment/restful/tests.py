from django.test import TestCase
from rest_framework.test import APIRequestFactory

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restfulexperiment.restful.models import User

import datetime


class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('user')
        data = {
        "name": "Joao da Silva",
        "email": "joao@silva.org",
        "password": "hunter2",
        }


        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Joao da Silva')

    def test_created_user_has_created_and_modified_date(self):
        """
        Ensure we can create a new user object, and that it has the same created and
        modified date.
        """
        url = reverse('user')
        data = {
        "name": "Joao da Silva",
        "email": "joao@silva.org",
        "password": "hunter2",
        }

        today = datetime.date.today()
        self.client.post(url, data, format='json')

        self.assertEqual(User.objects.get().modified, today)
        self.assertEqual(User.objects.get().created, today)
        self.assertEqual(User.objects.get().last_login, today)

    def test_created_user_has_token(self):
        """
        Ensure we can create a new user object, and that it has the same created and
        modified date.
        """
        url = reverse('user')
        data = {
        "name": "Joao da Silva",
        "email": "joao@silva.org",
        "password": "hunter2",
        }

        today = datetime.date.today()
        self.client.post(url, data, format='json')

        self.assertNotEqual(User.objects.get().token, '')


    def test_cant_create_two_users_with_same_email(self):
        url = reverse('user')
        user1 = {
        "name": "Joao da Silva",
        "email": "joao@silva.org",
        "password": "hunter2",
        }

        user2 = {
        "name": "Joao da Silva",
        "email": "joao@silva.org",
        "password": "hunter2",
        }

        self.client.post(url, user1, format='json')
        response = self.client.post(url, user2, format='json')

        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_login_ok(self):
        url = reverse('user')
        user1 = {"name": "john", "email": "john@silva.org", "password": "hunter2"}
        self.client.post(url, user1, format='json')

        url = reverse('login')
        data = {'email': "john@silva.org", "password": "hunter2"}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().name, 'john')


    def test_login_wrong_email(self):
        url = reverse('login')
        data = {'email': "wrong@email.org", "password": "wrongpassword"}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json, {'mensagem': "Usuário e/ou senha inválidos"})


    def test_login_wrong_password(self):
        url = reverse('user')
        user1 = {"name": "john", "email": "john@silva.org", "password": "hunter2"}
        self.client.post(url, user1, format='json')

        url = reverse('login')
        data = {'email': "john@silva.org", "password": "wrongpassword"}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json, {'mensagem': "Usuário e/ou senha inválidos"})


    def test_get_user_without_token(self):
        url = reverse('user')
        data = {
        "name": "Joao da Silva",
        "email": "joao@silva.org",
        "password": "hunter2",
        }
        self.client.post(url, data, format='json')

        url = reverse('user', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_user(self):
        url = reverse('user')
        data = {
        "name": "Joao da Silva",
        "email": "joao@silva.org",
        "password": "hunter2",
        }
        self.client.post(url, data, format='json')

        url = reverse('user', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().name, 'Joao da Silva')
