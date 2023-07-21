from django.utils.translation import gettext_lazy as _

from rest_framework.permissions import IsAdminUser


__all__ = (
    'IsSuperUser',
)


class IsSuperUser(IsAdminUser):
    """
    Custom DRF permission class that allows access only to superusers.

    This permission class is derived from `IsAdminUser` permission class provided by Django Rest Framework.
    It extends the functionality of `IsAdminUser` by allowing access only to users who have the `is_superuser` flag set to True.

    Methods:
        has_permission: Check if the request user is a superuser and has permission to access the view.
                        Overrides the parent class method.
    """

    message = _('You can not access this view.')

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
