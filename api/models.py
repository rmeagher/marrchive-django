from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

# class CustomUser(AbstractUser):
#     favorite_books = models.ManyToManyField('Book', related_name='user_favorites')
#     read_books = models.ManyToManyField('Book', related_name='users_have_read')
#     owned_books = models.ManyToManyField('Book', related_name='users_own')


class Book(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField('Author', related_name='books')
    # categories = models.ManyToManyField('Category', related_name='books')

    class JSONAPIMeta:
        resource_name = "books"


class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100,  null=True, blank=True)

    class JSONAPIMeta:
        resource_name = "authors"


class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)

    class JSONAPIMeta:
        resource_name = "Categories"
