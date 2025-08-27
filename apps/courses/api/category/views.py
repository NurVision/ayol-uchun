from django.db.models import Count
from rest_framework import generics

from apps.courses.models import Category

from .serializers import CategoryDetailSerializer, CategoryListSerializer


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        queryset = Category.objects.annotate(courses_count=Count("courses"))
        ids = self.request.query_params.get("ids")
        if ids:
            id_list = [int(i) for i in ids.split(",") if i.isdigit()]
            queryset = queryset.filter(id__in=id_list)
        return queryset


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

__all__ = ["CategoryDetailAPIView", "CategoryListAPIView"]

