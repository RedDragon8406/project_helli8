from rest_framework import filters
from rest_framework import viewsets
from main import models
from main import serializers
# Create your views here.
class UsermainViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserMainSerializer
    queryset = models.UserMain.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'app')