from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library_api import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
# path('snippets/<int:pk>/highlight/',
#      views.SnippetHighLight.as_view(), name='snippet-highlight'),
# path('users/', views.UserList.as_view(), name='user-list'),
# path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
