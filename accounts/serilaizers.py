from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer


__all__ = (
    'UserSerializer',
    'UserGetSerializer',
    'UserPostSerializer',
)

User = get_user_model()


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'date_joined',
        )
        read_only_fields = (
            'id',
            'is_staff',
            'is_active',
            'date_joined',
        )
        abstract = True


class UserSerializer(BaseUserSerializer):
    pass


class UserGetSerializer(BaseUserSerializer):
    pass


class UserPostSerializer(BaseUserSerializer):
    pass
