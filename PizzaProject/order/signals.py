from django.db.models.signals import post_save
from django.dispatch import receiver

from PizzaProject.emails import send_successful_order_email
from PizzaProject.order.models import OrderHistory


@receiver(post_save, sender=OrderHistory)
def order_created(sender, instance, created, **kwargs):
    if created:
        send_successful_order_email(instance.user)
