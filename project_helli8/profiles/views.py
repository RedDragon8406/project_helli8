from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles import serializers

class ApiView(APIView):
    """APIVIEW"""
    serializer_class = serializers.Serializer

    def get(self, request, format=None):
        """returns a list of api view features"""
        api_view = ["mamad", "jafar", "akbar", "asghar"]
        returning_dict = {
            "message": "sup mate",
            "view": api_view
        }

        return Response(returning_dict)
    def post(self, request):
        """create a message with a name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method":'PUT'})

    def patch(self, request, pk=None):
        """partial update of an object"""
        return Response({"method":'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method":'DELETE'})
