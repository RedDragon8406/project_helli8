from rest_framework import serializers
from product import models

class Serializer(serializers.Serializer):
    """Serializers a name field for testing our api view"""
    name = serializers.CharField(max_length=100)

class UserProductSerializer(serializers.ModelSerializer):
    """a user profile object"""

    class Meta:
        model = models.UserProduct
        fields = ('id', 'name', 'author','desc','img')

    def create(self, validated_data):
        """Create and return a new user"""
        product = models.UserProduct.objects.create_product(
            name=validated_data['name'],
            author=validated_data['author'],
            desc=validated_data['desc'],
            img=validated_data['img'],
        )

        return product