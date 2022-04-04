from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book, User, Book_Tracking, Note
from django.db.models import Q
from .permissions import IsAuthenticatedOrReadOnly
from .serializers import BookSerializer, UserSerializer, Book_TrackingSerializer, NoteSerializer
from rest_framework import filters
from rest_framework.decorators import action

from library_api import serializers


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
        'book trackers': reverse('book-tracking-list', request=request, format=format),
        'want to read': reverse('want-to-read-list', request=request, format=format),
        'reading': reverse('reading-list', request=request, format=format),
        'reading/done': reverse('reading-done-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format),
        'public notes': reverse('public-note-list', request=request, format=format),
        'featured books': reverse('featured', request=request, format=format),
    })


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Book_TrackingList(generics.ListCreateAPIView):

    serializer_class = Book_TrackingSerializer
    permission_classes = (
        permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

    def get_queryset(self):
        return Book_Tracking.objects.filter(user_id=self.request.user)


class WTRList(generics.ListCreateAPIView):

    serializer_class = Book_TrackingSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get_queryset(self):
        filters = Q(status='Want To Read') & Q(user_id=self.request.user)
        return Book_Tracking.objects.filter(filters)


class RList(generics.ListCreateAPIView):

    serializer_class = Book_TrackingSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get_queryset(self):
        filters = Q(status='Reading') & Q(user_id=self.request.user)
        return Book_Tracking.objects.filter(filters)


class RDList(generics.ListCreateAPIView):

    serializer_class = Book_TrackingSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get_queryset(self):
        filters = Q(status='Reading/Done') & Q(user_id=self.request.user)
        return Book_Tracking.objects.filter(filters)


class Book_TrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book_Tracking.objects.all()
    serializer_class = Book_TrackingSerializer
    permission_classes = (
        permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Featured(generics.ListCreateAPIView):
    queryset = Book.objects.all().filter(featured=True)
    serializer_class = BookSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class NoteList(generics.ListCreateAPIView):

    serializer_class = NoteSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Note.objects.filter(filters).order_by('-created_date')


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (
        permissions.IsAuthenticated,)


class PublicNotes(generics.ListCreateAPIView):
    filters = Q(public=True)
    queryset = Note.objects.all().filter(filters)
    serializer_class = NoteSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    #         @action(detail=False, methods=['GET'])
    # def featured(self, request):
    #     books = self.get_queryset().filter(feautured=True)
    #     serializer = self.get_serializer(books, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_serializer_class(self):
    #     if self.action in ['list', 'public']:
    #         return NoteSerializer
    #     return super().get_serializer_class()

    # @action(detail=False, methods=['GET'])
    # def public_notes(self, request):
    #     filters = Q(public=True)
    #     notes = self.get_queryset().filter(filters)
    #     serializer = self.get_serializer(notes, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
