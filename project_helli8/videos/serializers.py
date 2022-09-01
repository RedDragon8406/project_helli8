from collections import OrderedDict

from rest_framework import serializers
from videos import models


class VideoSerializer(serializers.ModelSerializer):
    """a user profile object"""
    video = serializers.CharField(max_length=200)
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.UserVideo
        fields = ("__all__")

    def create(self, validated_data):
        video = models.UserVideo.objects.create_video(validated_data)
        return video
    def show(self, instance):
        data = super(serializers.ModelSerializer, self).show(instance)
        result = OrderedDict()
        result['data'] = data
        result['message'] = 'Done'
        result['status'] = 'sucssed'
        return result
