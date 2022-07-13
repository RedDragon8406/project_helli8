from rest_framework import filters
from rest_framework import viewsets
from videos import models
from videos import serializers
class VideoViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.VideoSerializer
    queryset = models.UserVideo.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title')