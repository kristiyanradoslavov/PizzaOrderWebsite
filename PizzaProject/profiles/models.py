from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from PizzaProject.profiles.validators import letter_validator, phone_validator, validate_file_size

UserModel = get_user_model()


class Profile(models.Model):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 2
    PHONE_MAX_LENGTH = 12
    PHONE_MIN_LENGTH = 9
    CITY_MAX_LENGTH = 20
    CITY_MIN_LENGTH = 2
    ADDRESS_MAX_LENGTH = 30
    ADDRESS_MIN_LENGTH = 5

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LENGTH),
            letter_validator,
        ),
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LENGTH),
            letter_validator,
        ),
        blank=False,
        null=False,
    )

    phone_number = models.CharField(
        max_length=PHONE_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(PHONE_MIN_LENGTH),
            phone_validator,
        ),
        blank=False,
        null=False,
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(CITY_MIN_LENGTH),
        ),
        blank=False,
        null=False,
    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(CITY_MIN_LENGTH),
        ),
        blank=False,
        null=False,
    )

    image = models.ImageField(
        blank=True,
        null=True,
        upload_to='images/profiles/',
        validators=(
            validate_file_size,
        )
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )
