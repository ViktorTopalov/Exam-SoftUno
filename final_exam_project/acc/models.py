from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from final_exam_project.acc.managers import ProjectUserManager


class ProjectUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(_("email"), unique=True, max_length=150)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = ProjectUserManager()


