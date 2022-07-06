from rest_framework import serializers
from cat import models

class Serializer(serializers.Serializer):
    """Serializers a name field for testing our api view"""
    name = serializers.CharField(max_length=50)

class UserCatSerializer(serializers.ModelSerializer):
    """a user profile object"""

    class Meta:
        model = models.UserCat
        fields = ('id','name')

    def create(self, validated_data):
        """Create and return a new user"""
        cat = models.UserCat.objects.create_cat(
            name=validated_data['name'],
        )

        return cat