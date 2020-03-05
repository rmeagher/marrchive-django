from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    # category
    favorite = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    own = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)


class Author(models.Model):
    first = models.CharField(max_length=100, null=True, blank=True)
    last = models.CharField(max_length=100,  null=True, blank=True)


# class Favorite(models.Model):
#    book = models.ForeignKey('Book', on_delete=models.SET_NULL)
#    user = models.ForeignKey('User', on_delete=models.SET_NULL)


class Category(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
