from rest_framework import filters
from rest_framework import viewsets
from cat import models
from cat import serializers
# Create your views here.
class UserCatManager(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserCatSerializer
    queryset = models.UserCat.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)