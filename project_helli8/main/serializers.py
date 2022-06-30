from rest_framework import serializers
from product import models

class Serializer(serializers.Serializer):
    """Serializers a name field for testing our api view"""
    name = serializers.CharField(max_length=100)

class UserMainSerializer(serializers.ModelSerializer):
    """a user profile object"""

    class Meta:
        model = models.UserMain
        fields = ('id', 'name', 'author','desc')

    def create(self, validated_data):
        """Create and return a new user"""
        main = models.UserMain.objects.create_main(
            name=validated_data['name'],
            app=validated_data['app'],
            desc=validated_data['desc']
        )

        return product