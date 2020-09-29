from datetime import timedelta

from rest_framework.test import (
    APITestCase,
)
from rest_framework import status, reverse
from django.utils import timezone
from oauth2_provider.models import AccessToken
from django.urls import reverse
from CD.api.models import (
    Section,
)


def auth_data(cls):
    cls.access_token = AccessToken.objects.create(
        scope="read write",
        expires=timezone.now() + timedelta(seconds=300),
        token="secret-access-token-key",
    )


class LocationTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        auth_data(cls)

    def setUp(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token.token}')

    def test_it_rejects_location_with_invalid_x(self):
        url = reverse('api:location-list')
        data = {'label': 'A location',
                'x': 40000000.0,
                'y': 100.0,
                'z': 10000000.0,
                }
        request = self.client.post(url, data)
        self.assertEquals(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_it_rejects_location_with_invalid_y(self):
        url = reverse('api:location-list')
        data = {'label': 'A location with invalid y',
                'x': 30000000.0,
                'y': 255.1,
                'z': 10000000.0,
                }
        request = self.client.post(url, data)
        self.assertEquals(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_it_rejects_location_with_invalid_z(self):
        url = reverse('api:location-list')
        data = {'label': 'A location with invalid z',
                'x': 30000000.0,
                'y': 100.0,
                'z': 40000000.0,
                }
        request = self.client.post(url, data)
        self.assertEquals(request.status_code, status.HTTP_400_BAD_REQUEST)


class PageTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        auth_data(cls)
        cls.section = Section.objects.create(name='Towns')

    def setUp(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token.token}')

    def test_it_rejects_page_type_town_without_a_town(self):
        url = reverse('api:page-list')
        data = {'title': 'A Town page without a Town',
                'body': 'TestBody',
                'section': self.section.pk,
                'type': 3
                }
        request = self.client.post(url, data)
        self.assertEquals(request.status_code, status.HTTP_400_BAD_REQUEST)
