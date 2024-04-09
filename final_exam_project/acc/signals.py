from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from final_exam_project.profile.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created_event(sender, instance, created, **kwargs):
    if not created:
        return

    Profile.objects.create(user=instance)
