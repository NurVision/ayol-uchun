from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'phone_number': attrs.get('phone_number'),
            'password': attrs.get('password')
        }

        user = authenticate(**credentials)
        
        if user:
            if not user.is_active:
                raise serializers.ValidationError('Foydalanuvchi hisobi faol emas')
            if user.is_deleted:
                raise serializers.ValidationError('Foydalanuvchi hisobi o\'chirilgan')
                
            data = super().validate(attrs)
            data['user'] = {
                'id': user.id,
                'phone_number': user.phone_number,
                'username': user.username,
                'is_confirmed': user.is_confirmed
            }
            return data
        raise serializers.ValidationError('Telefon raqam yoki parol noto\'g\'ri')