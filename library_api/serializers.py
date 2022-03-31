from rest_framework import serializers
from .models import Book, Book_Tracking, User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date',
                  'genre', 'featured', 'owner',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'book',)


class Book_TrackingSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book_Tracking
        fields = ('status', 'user', 'book', 'owner',)
