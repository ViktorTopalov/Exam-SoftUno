from django.db import models

from final_exam_project.author.models import Author


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
    genre = models.CharField(max_length=50, choices = FANTASY_GENRES, null=False, blank=False)
    description = models.TextField()
    picture = models.URLField(
        null=True,
        blank=True
    )
    author = models.ForeignKey(Author, null=False, blank=False, on_delete=models.CASCADE)
