from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from PizzaProject import settings


def send_successful_registration_email(user):
    html_message = render_to_string(
        'emails/new_registration_email.html',
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


def send_successful_order_email(user):
    html_message = render_to_string(
        'emails/new_order_email.html',
        {'user': user},
    )

    plain_message = strip_tags(html_message)

    send_mail(
        subject='Order successful!',
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,),
    )
