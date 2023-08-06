from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from PizzaProject import settings
from PizzaProject.profiles.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile_on_register(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )


def send_successful_registration_email(user):
    html_message = render_to_string(
        'pass',
        {'user': user},
    )

    plain_message = strip_tags(html_message)

    send_mail(
        subject='Registration successful!',
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,),
    )


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)
