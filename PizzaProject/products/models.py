from django.core import validators
from django.db import models
from django.template.defaultfilters import slugify

from PizzaProject.products.validators import name_validator, positive_price


class BaseProduct(models.Model):
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2
    DESCRIPTION_MAX_LEN = 100
    DESCRIPTION_MIN_LEN = 5

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            name_validator,
            validators.MinLengthValidator(NAME_MIN_LEN)
        ),
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        validators=(
            validators.MinLengthValidator(DESCRIPTION_MIN_LEN),
        ),
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name} - {self.id}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    @classmethod
    def get_subclass_models(cls):
        # Get all subclasses of the Product model
        subclasses = cls.__subclasses__()

        return subclasses


class Pizza(BaseProduct):
    STRIPE_PRICE_MAX_LEN = 100

    price_small = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    price_medium = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    price_large = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    price_extra_large = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    stripe_small_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    stripe_medium_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    stripe_large_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    stripe_extra_large_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        blank=True,
        null=True,
        upload_to='images/products/pizzas',
    )


class Salad(BaseProduct):
    STRIPE_PRICE_MAX_LEN = 100

    price_small = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    price_large = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    stripe_small_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    stripe_large_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        null=False,
        blank=False,
        upload_to='images/products/salads'
    )


class Desert(BaseProduct):
    STRIPE_PRICE_MAX_LEN = 100

    price = models.FloatField(
        validators=(
            positive_price,
        ),
        blank=False,
        null=False,
    )

    stripe_single_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to='images/products/deserts',
        null=False,
        blank=False,
    )


class Drink(BaseProduct):
    STRIPE_PRICE_MAX_LEN = 100

    price_small = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    price_large = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    stripe_small_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    stripe_large_price_id = models.CharField(
        max_length=STRIPE_PRICE_MAX_LEN,
        null=True,
        blank=True,
    )

    small_image = models.ImageField(
        null=False,
        blank=False,
        upload_to='images/products/drink'
    )

    large_image = models.ImageField(
        null=False,
        blank=False,
        upload_to='images/products/images'
    )
