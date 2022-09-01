from rest_framework import serializers
from profiles import models
from collections import OrderedDict
class Serializer(serializers.Serializer):
    """Serializers a name field for testing our api view"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """a user profile object"""
    product = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = models.UserProfile
        fields = ('id','email','password','name','img','is_staff','is_active','groups','product','favorite')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            img=validated_data['img'],
            is_staff=validated_data['is_staff']
        )

        return user

    def show(self, instance):
        data = super(serializers.ModelSerializer, self).show(instance)
        result = OrderedDict()
        result['data'] = data
        result['message'] = 'Done'
        result['status'] = 'sucssed'
        return result