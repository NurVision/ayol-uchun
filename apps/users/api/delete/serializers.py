from rest_framework import serializers
from apps.users.choices import ReasonDeleteChoices

class UserDeleteSerializer(serializers.Serializer):
    reason_delete_choices = serializers.ChoiceField(
        choices=ReasonDeleteChoices.choices,
        required=False,
        allow_null=True
    )
    reason_delete_str = serializers.CharField(
        max_length=100,
        required=False,
        allow_null=True,
        allow_blank=True
    )
    password = serializers.CharField(write_only=True, required=True)