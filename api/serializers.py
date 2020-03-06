from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField


from api.models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    included_serializers = {'books': 'api.serializers.BookSerializer'}

    class Meta:
        model = Author
        fields = ['id', 'url', 'first_name', 'last_name']
        extra_kwargs = {'books': {'required': False}}


class BookSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {'authors': AuthorSerializer}
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        authors = ResourceRelatedField(
            queryset=Author.objects,
            many=True,
            related_link_view_name='book-author-detail',
            related_link_url_kwarg='author_pk',
            self_link_view_name='book-relationships'

        )
        fields = ['id', 'url', 'title', 'authors', 'description', 'notes']
        extra_kwargs = {'books': {'required': False}}

    # class JSONAPIMeta:
    #     this is only needed if you want the resource to be included by default
    #     included_resources = ['authors']

    # def create(self, validated_data):
    #     authors_data = validated_data.pop('authors')
    #     book = Book.objects.create(**validated_data)
    #     for author_data in authors_data:
    #         Author.objects.create(book=book, **author_data)
    #     return book
    #
    # def update(self, instance, validated_data):
    #     authors_data = validated_data.pop('authors')
    #     # https://django.cowhite.com/blog/create-and-update-django-rest-framework-nested-serializers/


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description']
