from rest_framework import serializers

from apps.users.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'bio',
            'interests',
        ]
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': False},
        }

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value, is_deleted=False).exists():
            raise serializers.ValidationError("Ushbu foydalanuvchi nomi band")
        return value