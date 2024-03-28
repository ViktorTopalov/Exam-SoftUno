from django.db import models


class Author(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    nationality = models.CharField(max_length=35, null=False, blank=False)

    date_of_death = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    biography = models.TextField(blank=True)
