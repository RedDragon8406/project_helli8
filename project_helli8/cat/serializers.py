from rest_framework import serializers
from cat import models

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