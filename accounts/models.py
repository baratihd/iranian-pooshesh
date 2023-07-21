from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import phone_number_validator
from .constants import verbose_names


class User(AbstractUser):
    phone_number = models.CharField(
        verbose_name=verbose_names.PHONE_NUMBER,
        validators=[phone_number_validator],
        max_length=11,
        unique=True,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return '{} {}'.format(self.username, self.get_full_name())
