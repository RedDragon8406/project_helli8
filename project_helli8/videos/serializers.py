from rest_framework import serializers
from videos import models

class Serializer(serializers.Serializer):
    """Serializers a name field for testing our api view"""
    title = serializers.CharField(max_length=100)



class VideoSerializer(serializers.ModelSerializer):
    """a user profile object"""

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
