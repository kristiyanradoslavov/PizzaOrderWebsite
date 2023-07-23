from django.core import validators
from django.db import models
from django.template.defaultfilters import slugify

from PizzaProject.products.validators import name_validator, positive_price


class Pizza(models.Model):
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2
    DESCRIPTION_MAX_LEN = 100
    DESCRIPTION_MIN_LEN = 5

    SIZE_CHOICES = (
        'Small',
        'Medium',
        'Large',
        'Extra Large',
    )

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

    image = models.ImageField(
        blank=True,
        null=True,
        upload_to='images/products/pizzas',
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


class Salad(models.Model):
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 2
    DESCRIPTION_MAX_LEN = 100
    DESCRIPTION_MIN_LEN = 5

    SIZE_CHOICES = (
        'Small',
        'Large',
    )

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
            name_validator,
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

    small_price = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    large_price = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    image = models.ImageField(
        null=False,
        blank=False,
        upload_to='images/products/salads'
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


class Desert(models.Model):
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2
    DESCRIPTION_MAX_LEN = 100
    DESCRIPTION_MIN_LEN = 5

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
            name_validator,
        ),
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        validators=(
            validators.MinLengthValidator(DESCRIPTION_MIN_LEN),
        ),
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=(
            positive_price,
        ),
        blank=False,
        null=False,
    )

    image = models.ImageField(
        upload_to='images/products/deserts',
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


class Drink(models.Model):
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 2
    DESCRIPTION_MAX_LEN = 100
    DESCRIPTION_MIN_LEN = 5

    SIZE_CHOICES = (
        'Small',
        'Large',
    )

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
            name_validator,
        ),
        null=False,
        blank=False,
    )

    small_price = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    large_price = models.FloatField(
        validators=(
            positive_price,
        ),
        null=False,
        blank=False,
    )

    small_image = models.ImageField(
        null=False,
        blank=False,
        upload_to='images/products/images'
    )

    large_image = models.ImageField(
        null=False,
        blank=False,
        upload_to='images/products/images'
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
