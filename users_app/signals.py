from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def profile_create(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
        )


@receiver(post_save, sender=Profile)
def user_update(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.first_name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def profile_delete(sender, instance, **kwargs):
    user = instance.user
    user.delete()
