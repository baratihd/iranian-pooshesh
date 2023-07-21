from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from common.permissions import IsSuperUser
from common.mixins import CustomPaginationMixin
from .serilaizers import UserSerializer, UserGetSerializer, UserPostSerializer


__all__ = (
    'UserViewSet',
)


User = get_user_model()


class UserViewSet(CustomPaginationMixin, ModelViewSet):
    """
    ModelViewSet for managing user data.

    It provides different serializers based on the action being performed (GET or POST).
    Additionally, it sets custom pagination keys for the paginated response.
    """

    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the action being performed.
        """

        if self.action in {'list', 'retrieve'}:
            return UserGetSerializer
        if self.action == 'created':
            return UserPostSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        """
        Return the appropriate permission classes based on the action being performed.
        """

        if self.action == 'list':
            self.permission_classes = (IsSuperUser,)
        elif self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

    def get_custom_pagination_keys(self):
        """
        Provide custom key-value pairs for the response.
        """

        keys = {
            'key1': 'value1',
            'key2': 'value2',
        }
        return keys
