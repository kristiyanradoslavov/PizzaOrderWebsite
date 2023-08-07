from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from PizzaProject.emails import send_successful_registration_email
from PizzaProject.profiles.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile_on_register(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)
