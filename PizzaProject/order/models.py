from django.db import models


class OrderItem(models.Model):
    TYPE_MAX_LEN = 20
    product_type = models.CharField(
        max_length=TYPE_MAX_LEN,
        null=False,
        blank=False,
    )

    product_id = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
