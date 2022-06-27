from rest_framework import filters
from rest_framework import viewsets
from product import models
from product import serializers
# Create your views here.
class UserProductViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProductSerializer
    queryset = models.UserProduct.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'author')