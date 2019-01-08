from django.contrib.auth.models import User
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerialiser


class SnippetList(generics.ListCreateAPIView):
    """    List all code snippets, or create a new snippet."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a snippet instance."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
