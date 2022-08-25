from rest_framework import serializers
from topic import models
from collections import OrderedDict

class UserTopicSerializer(serializers.ModelSerializer):
    """a user profile object"""
    products = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = models.UserTopic
        fields = ('__all__')

    def create(self, validated_data):
        """Create and return a new user"""
        print(validated_data)
        topic = models.UserTopic.objects.create(**validated_data)
        # product.categories.set(**validated_data["categories"])
        return topic

    def show(self, instance):
        data = super(serializers.ModelSerializer, self).show(instance)
        result = OrderedDict()
        result['data'] = data
        result['message'] = 'Done'
        result['status'] = 'sucessed'
        return result

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('title', instance.name)
        instance.img = validated_data.get('img', instance.img)
        instance.categories = validated_data.get('products', instance.products)
        instance.save()
        return instance


