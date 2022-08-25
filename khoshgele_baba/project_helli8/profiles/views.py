from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles import models
from rest_framework.authentication import TokenAuthentication
from profiles import permissions
from profiles import serializers
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class ApiView(APIView):
    """APIVIEW"""
    serializer_class = serializers.Serializer

    def get(self, request, format=None):
        """returns a list of api view features"""
        api_view = ["mamad", "jafar", "akbar", "asghar"]
        returning_dict = {
            "message": "sup mate",
            "view": api_view,
        }

        return Response(returning_dict)

    def post(self, request):
        """create a message with a name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": 'PUT'})

    def patch(self, request, pk=None):
        """partial update of an object"""
        return Response({"method": 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": 'DELETE'})


class ViewSet(viewsets.ViewSet):
    """api viewset"""
    serializer_class = serializers.Serializer

    def list(self, request):
        """return a message"""

        the_viewsets = [
            'Mark',
            'Kevin',
            'Johnathon',
            'Timmy',
            'Arthur'
        ]

        return Response({'message': 'message hehe', 'viewsets': the_viewsets})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle retrieving an object"""
        return Response({'http_method': 'GET'})

    def uptade(self, request, pk=None):
        """Handle updating an object"""
        return Response({'https_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'http_method': "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email','password', 'is_staff')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from profiles.models import UserProfile
from profiles.serializers import UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def profile_list(request):

    if request.method == 'GET':
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return JsonResponse(serializer.data)
@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):
    """
    Retrieve, update or delete a code profile.
    """
    try:
        profile = UserProfile.objects.get(pk=pk)
    except profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
