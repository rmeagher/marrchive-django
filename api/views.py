from django.shortcuts import render

from django.contrib.auth.models import User, Group
from api.models import Author, Book
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import BookSerializer, AuthorSerializer, CategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [permissions.IsAuthenticated]
