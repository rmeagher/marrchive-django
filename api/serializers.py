from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField


from api.models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {'authors': AuthorSerializer,
                            'categories': CategorySerializer}
    authors = AuthorSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Book
        authors = ResourceRelatedField(
            queryset=Author.objects.all(),
            related_link_view_name='book-author-detail',
            related_link_url_kwarg='author_pk',
            self_link_view_name='book-relationships'

        )
        fields = ['url', 'title', 'authors', 'categories', 'description', 'notes']

    class JSONAPIMeta:
        included_resources = ['authors']

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        for author_data in authors_data:
            Author.objects.create(book=book, **author_data)
        return book

    def update(self, instance, validated_data):
        authors_data = validated_data.pop('authors')
    https://django.cowhite.com/blog/create-and-update-django-rest-framework-nested-serializers/
