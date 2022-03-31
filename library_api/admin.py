from django.contrib import admin
from .models import User, Book, Book_Tracking


admin.site.register(User)
admin.site.register(Book)
admin.site.register(Book_Tracking)
