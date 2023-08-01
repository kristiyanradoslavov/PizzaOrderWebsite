from django.core.exceptions import ValidationError


def name_validator(value):
    for v in value:
        if not v.isalpha():
            raise ValidationError("The name can contain only letters.")


def positive_price(value):
    if value <= 0:
        raise ValidationError("The value cannot be less than or equal to 0")