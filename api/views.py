from django.shortcuts import render

from django.contrib.auth.models import User, Group
from api.models import Author, Book
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import BookSerializer, AuthorSerializer, CategorySerializer
from rest_framework_json_api.views import RelationshipView


class BookRelationshipView(RelationshipView):
    queryset = Book.objects
    self_link_view_name = 'book-relationships'
    # permission_classes = [permissions.IsAuthenticated]


class AuthorRelationshipView(RelationshipView):
    queryset = Author.objects
    self_link_view_name = 'author-relationships'
    # permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that for the Author models.

    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for the Book models.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]
