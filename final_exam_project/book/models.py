from django.contrib.auth import get_user_model
from django.db import models

from final_exam_project.profile.models import Profile

UserModel = get_user_model()


class Book(models.Model):
    FANTASY_GENRES = (
        ('High Fantasy', 'High Fantasy'),
        ('Low Fantasy', 'Low Fantasy'),
        ('Epic Fantasy', 'Epic Fantasy'),
        ('Dark Fantasy', 'Dark Fantasy'),
        ('Historical Fantasy', 'Historical Fantasy'),
        ('Magical Realism', 'Magical Realism'),
        ('Portal Fantasy', 'Portal Fantasy'),
        ('Grimdark Fantasy', 'Grimdark Fantasy'),
        ('Science Fantasy', 'Science Fantasy'),
        ('Fairy Tale Fantasy', 'Fairy Tale Fantasy'),
        ('Mythological Fantasy', 'Mythological Fantasy'),
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    publication_date = models.DateField(null=False, blank=False)
    genre = models.CharField(max_length=50, choices=FANTASY_GENRES, null=False, blank=False)
    description = models.TextField()
    author = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    picture = models.URLField(
        null=True,
        blank=True
    )
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='liking_books')
    created_at = models.DateTimeField(auto_now_add=True)
