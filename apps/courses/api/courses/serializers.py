from rest_framework import serializers
from django.utils import timezone
from apps.courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    remaining_time = serializers.SerializerMethodField()
    category = serializers.StringRelatedField() 

    class Meta:
        model = Course
        fields = ["id", "title", "description", "price", "old_price", "card", "category", "rating", "speaker", "discount_end", "remaining_time"]

    def get_remaining_time(self, obj):
        if obj.discount_end and obj.discount_end > timezone.now():
            remaining = obj.discount_end - timezone.now()
            days = remaining.days
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, _ = divmod(remainder, 60)

            return f"{days}d {hours}h {minutes}m"
        return None

