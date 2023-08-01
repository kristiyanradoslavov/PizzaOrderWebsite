from django.core.exceptions import ValidationError


def letter_validator(value):
    for v in value:
        if (not v.isalpha()) and (v != '-'):
            raise ValidationError("The name can contain only letters and ' - '(dash)")


def phone_validator(value):
    error_messages = []
    if value[0] != '0' and value[:3] != '359':
        error_messages.append("Phone number must start with '359' or '0' !")
    for v in value:
        if not v.isdigit():
            error_messages.append('Phone number must contain only digits !')

    if error_messages:
        raise ValidationError('\n'.join(error_messages))


def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")