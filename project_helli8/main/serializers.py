from rest_framework import serializers
from main import models

class Serializer(serializers.Serializer):
    """Serializers a name field for testing our api view"""
    app = serializers.CharField(max_length=100)

class UserMainSerializer(serializers.ModelSerializer):
    """a user profile object"""

    class Meta:
        model = models.UserMain
        fields = ('app',)

    def create(self, validated_data):
        """Create and return a new user"""
        main = models.UserMain.objects.create_main(
            app=validated_data['app'],
        )

        return main