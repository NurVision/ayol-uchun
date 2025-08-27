from rest_framework import generics
from django.db.models import Q
from apps.courses.models import Course
from .serializers import CourseSerializer


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        categories = self.request.query_params.get("categories")
        if categories:
            category_ids = [int(cat_id) for cat_id in categories.split(",") if cat_id.isdigit()]
            queryset = queryset.filter(category_id__in=category_ids)
        return queryset


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


__all__ = ["CourseListAPIView", "CourseDetailAPIView"]