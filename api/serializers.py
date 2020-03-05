from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField


from api.models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first', 'last']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {'author': AuthorSerializer}

    class Meta:
        model = Book
        author = ResourceRelatedField(
            queryset=Author.objects,
            related_link_view_name='book-author-detail',
            related_link_url_kwarg='author_pk',
            self_link_view_name='book-relationships'
                                      )
        fields = ['url', 'title', 'author', 'description', 'read', 'own', 'favorite', 'notes']

    class JSONAPIMeta:
        included_resources = ['author']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description']
