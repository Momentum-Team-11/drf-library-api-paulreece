from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    genre = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="books",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_book")
        ]


class Book_Tracking(models.Model):
    WANT_TO_READ = 'Want To Read'
    READING = 'Reading'
    READING_DONE = 'Read/Done'
    STATUS_CHOICES = [(WANT_TO_READ, 'Want To Read'),
                      (READING, 'Reading'), (READING_DONE, 'Read/Done')]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="book_tracking",
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="library_book",
    )

    def __str__(self):
        return f"{self.status} {self.user} {self.book}"


class Note(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, null=True, related_name="notes")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notes",
    )
    created_date = models.DateTimeField(auto_now_add=datetime.now)
    text = models.CharField(max_length=2000)
    public = models.BooleanField(default=False)
    page_number = models.IntegerField(blank=True, null=True)
