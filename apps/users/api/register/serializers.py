from rest_framework import serializers

from apps.users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'phone_number',
            'username',
            'password',
            'password2',
            'email',
            'first_name',
            'last_name',
        ]
        extra_kwargs = {
            'phone_number': {'required': True},
            'username': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Passwordlar mos kelmayapti"}
            )
        
        if User.objects.filter(username=attrs['username'], is_deleted=False).exists():
            raise serializers.ValidationError(
                {"username": "Ushbu foydalanuvchi nomi band"}
            )
            
        if User.objects.filter(phone_number=attrs['phone_number'], is_deleted=False).exists():
            raise serializers.ValidationError(
                {"phone_number": "Ushbu telefon raqam ro'yxatdan o'tgan"}
            )
            
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user