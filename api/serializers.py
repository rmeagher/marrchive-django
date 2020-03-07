from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField


from api.models import Book, Author, Category


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {'books': 'api.serializers.BookSerializer'}

    class Meta:
        model = Author
        fields = "__all__"
        extra_kwargs = {'books': {'required': False}}
    books = ResourceRelatedField(
        model=Book,
        queryset=Book.objects.all(),
        many=True,
        required=False,
        related_link_view_name='author-related',
        related_link_url_kwarg='pk',
        self_link_view_name='author-relationships'
    )


class BookSerializer(serializers.HyperlinkedModelSerializer):

    # authors = AuthorSerializer(many=True, read_only=True)
    included_serializers = {'authors': 'api.serializers.AuthorSerializer'}

    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {'authors': {'required': False}}
    authors = ResourceRelatedField(
        model=Author,
        queryset=Author.objects.all(),
        many=True,
        required=False,
        related_link_view_name='book-related',
        related_link_url_kwarg='pk',
        self_link_view_name='book-relationships'
        )

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
