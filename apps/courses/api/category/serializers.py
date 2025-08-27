from rest_framework import serializers

from apps.courses.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    courses_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "courses_count"]


class CategoryDetailSerializer(serializers.ModelSerializer):
    courses_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "courses_count"]
