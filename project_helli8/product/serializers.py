from rest_framework import serializers
from product import models
from collections import OrderedDict


class UserProductSerializer(serializers.ModelSerializer):
    """a user profile object"""
    categories = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.UserProduct
        fields = ('id', 'name', 'author','desc','img','categories','exist')

    def create(self, validated_data):
        """Create and return a new user"""
        product = models.UserProduct.objects.create_product(**validated_data)

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



