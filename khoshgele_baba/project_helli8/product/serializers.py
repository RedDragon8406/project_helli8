from rest_framework import serializers
from product import models
from collections import OrderedDict
from videos.models import UserVideo

class UserProductSerializer(serializers.ModelSerializer):
    """a user profile object"""
    categories = serializers.StringRelatedField(many=True,read_only=True)
    videos = serializers.StringRelatedField(many=True,read_only=True)
    podcasts = serializers.StringRelatedField(many=True,read_only=True)
    topic = serializers.CharField(read_only=True)
    class Meta:
        model = models.UserProduct
        fields = ('__all__')

    def create(self, validated_data):
        """Create and return a new user"""
        print(validated_data)
        product = models.UserProduct.objects.create(**validated_data)
        # product.categories.set(**validated_data["categories"])
        return product

    def show(self, instance):
        data = super(serializers.ModelSerializer, self).show(instance)
        result = OrderedDict()
        result['data'] = data
        result['message'] = 'Done'
        result['status'] = 'sucssed'
        return result

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.exist = validated_data.get('exist', instance.exist)
        instance.img = validated_data.get('img', instance.img)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.save()
        return instance



