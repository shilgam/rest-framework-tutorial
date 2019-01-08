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


class ListTests(APITestCase):
    def test_view(self):
        create_snippet(data)
        url = reverse('snippets:index')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create(self):
        url = reverse('snippets:index')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIs(Snippet.objects.count(), 1)


class DetailTests(APITestCase):
    def test_view(self):
        snippet = create_snippet(data)
        url = reverse('snippets:detail', args=(snippet.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], data['code'])

    def test_view_unexistent(self):
        create_snippet(data)
        url = reverse('snippets:detail', args=(99999999,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        content = {
            "detail": "Not found."
        }
        self.assertEqual(response.data, content)

    def test_update(self):
        snippet = create_snippet(data)
        url = reverse('snippets:detail', args=(snippet.id,))
        updated_data = {'code': 'print("Updated code")'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], updated_data['code'])

    def test_delete(self):
        snippet = create_snippet(data)
        url = reverse('snippets:detail', args=(snippet.id,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
