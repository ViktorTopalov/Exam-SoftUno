from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()
from final_exam_project.acc.models import ProjectUser


# Create your models here.
class Profile(models.Model):
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
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(21)],
        help_text="Age requirement: 21 years and above."
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True, )

