from django.core.exceptions import ValidationError


def validate_username(username):
    if not username.isalnum() or '_' in username:
        raise ValidationError("Username must contain only letters, digits, and underscores!")