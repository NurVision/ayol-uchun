from rest_framework import serializers
from django.utils import timezone
from apps.courses.models import Webinar


class WebinarSerializer(serializers.ModelSerializer):
    remaining_time = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Webinar
        fields = [
            "id",
            "title",
            "description",
            "price",
            "card",
            "category",
            "author",
            "datetime",
            "rating",
            "remaining_time",
        ]

    def get_remaining_time(self, obj):
        if obj.datetime and obj.datetime > timezone.now():
            remaining = obj.datetime - timezone.now()
            return remaining.total_seconds()
        return None
