from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from snippets.models import Snippet

data = {
        'title': 'Some Code',
        'code': "print('Hello, World!')",
    }


def create_snippet(attributes=data):
    return Snippet.objects.create(**attributes)


class SnippetTests(APITestCase):

    def test_create(self):
        url = reverse('snippets:index')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIs(Snippet.objects.count(), 1)

    def test_view_index(self):
        create_snippet(data)
        url = reverse('snippets:index')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_view_detail(self):
        snippet = create_snippet(data)
        url = reverse('snippets:detail', args=(snippet.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], data['code'])
