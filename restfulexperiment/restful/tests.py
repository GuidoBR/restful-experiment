from django.test import TestCase
from rest_framework.test import APIRequestFactory

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restfulexperiment.restful.models import User


class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('user', kwargs={'pk': 1})
        data = {
        "name": "Joao da Silva",
        "email": "joao@silva.org",
        "password": "hunter2",
        "phones": [
            {
                "number": "987654321",
                "ddd": "21"
                }
            ]
        }


        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Joao da Silva')

