from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField('Author', related_name='books')
    categories = models.ManyToManyField('Category', related_name='books')

    class JSONAPIMeta:
        resource_name = "books"


class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100,  null=True, blank=True)

    class JSONAPIMeta:
        resource_name = "authors"


class Favorite(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class JSONAPIMeta:
        resource_name = "favorites"


class Read(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Own(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
