from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

UserModel = get_user_model()


class OrderItem(models.Model):
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 3
    SIZE_MAX_LEN = 20
    SIZE_NIM_LEN = 3

    product_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
        ),
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

    size = models.CharField(
        max_length=SIZE_MAX_LEN,
        validators=(
            validators.MinLengthValidator(SIZE_NIM_LEN),
        ),
        null=True,
        blank=True,
    )

    single_price = models.FloatField(
        null=False,
        blank=False
    )

    image = models.ImageField(
        null=False,
        blank=False
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
