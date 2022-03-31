from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def __str__(self):
        return f"{self.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_book")
        ]


class Book_Tracking(models.Model):
    status = models.CharField(max_length=200)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="library_user",
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
