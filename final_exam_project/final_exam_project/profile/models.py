from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from final_exam_project.profile.validators import validate_username


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3,
                               message="Username must be at least 3 chars long!"),
            validate_username
        ],
        null=False,
        blank=False
    )
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
        MinValueValidator(21)],
        help_text= "Age requirement: 21 years and above."
    )
    password = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
    profile_picture = models.URLField(
        null=True,
        blank=True
    )



