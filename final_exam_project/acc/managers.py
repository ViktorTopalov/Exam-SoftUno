from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import models as auth_models


class ProjectUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

