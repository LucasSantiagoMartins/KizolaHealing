from django.core.exceptions import ValidationError


def phone_number_validator(value):

    try:
        int(value)
    except ValueError:
        raise ValidationError('The phone number must be integer.')
    