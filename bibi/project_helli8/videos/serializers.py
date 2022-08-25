from collections import OrderedDict

from rest_framework import serializers
from videos import models


class VideoSerializer(serializers.ModelSerializer):
    """a user profile object"""
    video = serializers.CharField(max_length=200)

    class Meta:
        model = models.UserVideo
        fields = ('id', 'title', 'video')

    def create(self, validated_data):
        """Create and return a new user"""
        video = models.UserVideo.objects.create_video(
            title=validated_data['title'],
            video=validated_data['video'],
        )

        return video
    def show(self, instance):
        data = super(serializers.ModelSerializer, self).show(instance)
        result = OrderedDict()
        result['data'] = data
        result['message'] = 'Done'
        result['status'] = 'sucssed'
        return result
