from rest_framework import serializers
from .models import Book, Book_Tracking, User, Note


class BookSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Book
        fields = ('url', 'title', 'author', 'publication_date',
                  'genre', 'featured', 'user', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True, view_name='book-detail', read_only=True)
    book_tracking = serializers.HyperlinkedRelatedField(
        many=True, view_name='book-tracking-list', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'books', "book_tracking")


class Book_TrackingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all())
    book = serializers.SlugRelatedField(
        slug_field="title", queryset=Book.objects.all())

    class Meta:
        model = Book_Tracking
        fields = ('url', 'status', 'book', 'user',)


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all())
    book = serializers.SlugRelatedField(
        slug_field="title", queryset=Book.objects.all())

    class Meta:
        model = Note
        fields = ('url', 'book', 'user', 'created_date', 'text', 'public', 'page_number', )
