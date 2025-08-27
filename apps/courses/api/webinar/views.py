from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.courses.models import Webinar
from .serializers import WebinarSerializer


class WebinarListAPIView(generics.ListAPIView):
    serializer_class = WebinarSerializer

    def get_queryset(self):
        queryset = Webinar.objects.all()
        categories = self.request.query_params.get("categories")
        if categories:
            category_ids = [int(cat_id) for cat_id in categories.split(",") if cat_id.isdigit()]
            queryset = queryset.filter(category_id__in=category_ids)
        return queryset


class WebinarDetailAPIView(generics.RetrieveAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class WebinarCreateAPIView(APIView):
    def post(self, request):
        serializer = WebinarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebinarUpdateAPIView(APIView):
    def put(self, request, pk):
        webinar = get_object_or_404(Webinar, pk=pk)
        serializer = WebinarSerializer(webinar, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        webinar = get_object_or_404(Webinar, pk=pk)
        serializer = WebinarSerializer(webinar, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebinarDeleteAPIView(APIView):
    def delete(self, request, pk):
        webinar = get_object_or_404(Webinar, pk=pk)
        webinar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ["WebinarListAPIView", "WebinarDetailAPIView", "WebinarCreateAPIView", "WebinarUpdateAPIView", "WebinarDeleteAPIView"]
