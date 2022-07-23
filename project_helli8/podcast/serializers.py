from rest_framework import serializers
from podcast import models


class VoiceSerializer(serializers.ModelSerializer):
    """a user profile object"""
    voice = serializers.CharField(max_length=200)

    class Meta:
        model = models.UserVoice
        fields = ('id', 'title', 'voice')

    def create(self, validated_data):
        """Create and return a new user"""
        voice = models.UserVoice.objects.create_video(
            title=validated_data['title'],
            video=validated_data['voice'],
        )

        return voice
