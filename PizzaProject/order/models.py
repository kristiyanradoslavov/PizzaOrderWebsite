from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

UserModel = get_user_model()


class BaseOrderModel(models.Model):
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 3
    SIZE_MAX_LEN = 20
    SIZE_NIM_LEN = 3
    PRICE_ID_MAX_LEN = 40

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
        null=True,
        blank=True,
    )

    price_id = models.CharField(
        max_length=PRICE_ID_MAX_LEN,
        null=False,
        blank=False,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.product_name

    class Meta:
        abstract = True


class OrderItem(BaseOrderModel):
    pass


class OrderHistory(BaseOrderModel):
    SPECIFIC_ORDER_ID_MAX_LEN = 60

    specific_order_id = models.CharField(
        max_length=SPECIFIC_ORDER_ID_MAX_LEN,
        editable=False,
        null=True,
        blank=True,
    )
