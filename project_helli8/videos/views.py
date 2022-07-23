from django.http import JsonResponse
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from videos import models
from videos import serializers
from videos.models import UserVideo
from videos.serializers import VideoSerializer

class VideoViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.VideoSerializer
    queryset = models.UserVideo.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title')





@api_view(['GET', 'POST'])
def video_list(request):

    if request.method == 'GET':
        videos = UserVideo.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)