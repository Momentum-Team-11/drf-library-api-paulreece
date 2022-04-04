from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library_api import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('book_trackers/', views.Book_TrackingList.as_view(),
         name='book-tracking-list'),
    path('book_trackers/want-to-read/', views.WTRList.as_view(),
         name='want-to-read-list'),
    path('book_trackers/reading/', views.RList.as_view(),
         name='reading-list'),
    path('book_trackers/reading-done/', views.RDList.as_view(),
         name='reading-done-list'),
    path('book_trackers/<int:pk>/', views.Book_TrackingDetail.as_view(),
         name='book_tracking-detail'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('featured/', views.Featured.as_view(), name='featured'),
    path('notes/', views.NoteList.as_view(),
         name='note-list'),
    path('public-notes/', views.PublicNotes.as_view(),
         name='public-note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(),
         name='note-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
# path('snippets/<int:pk>/highlight/',
#      views.SnippetHighLight.as_view(), name='snippet-highlight'),

# path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
