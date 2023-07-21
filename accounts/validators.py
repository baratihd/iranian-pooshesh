from django.core.exceptions import ValidationError

from .constants import messages


__all__ = (
    'phone_number_validator',
)


def phone_number_validator(phone_number: str) -> None:
    if phone_number and (not phone_number.isdigit() or not phone_number.startswith('09')):
        raise ValidationError(messages.PHONE_NUMBER_NOT_VALID)
