from rest_framework import serializers

class UserConfirmSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True, min_length=4, max_length=6)