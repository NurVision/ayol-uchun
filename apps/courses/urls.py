from django.urls import path

from apps.courses.api.webinar.views import WebinarCreateAPIView, WebinarDeleteAPIView, WebinarDetailAPIView, WebinarListAPIView, WebinarUpdateAPIView

from .api import (
    CategoryDetailAPIView, CategoryListAPIView,
    CourseDetailAPIView, CourseListAPIView
)

app_name = "courses"
urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("courses/", CourseListAPIView.as_view(), name="course-list"),
    path("courses/<int:pk>/", CourseDetailAPIView.as_view(), name="course-detail"),
    path("webinars/", WebinarListAPIView.as_view(), name="webinar-list"),
    path("webinars/<int:pk>/", WebinarDetailAPIView.as_view(), name="webinar-detail"),
    path("webinars/create/", WebinarCreateAPIView.as_view(), name="webinar-create"),
    path("webinars/<int:pk>/update/", WebinarUpdateAPIView.as_view(), name="webinar-update"),
    path("webinars/<int:pk>/delete/", WebinarDeleteAPIView.as_view(), name="webinar-delete"),
]