from rest_framework import serializers

from apps.users.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'phone_number',
            'username',
            'email',
            'first_name',
            'last_name',
            # 'avatar',
            'bio',
            'is_confirmed',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'phone_number', 'is_confirmed', 'created_at', 'updated_at']

