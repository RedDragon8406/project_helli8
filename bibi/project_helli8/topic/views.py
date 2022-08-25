from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from topic.models import UserTopic
from topic.serializers import UserTopicSerializer
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def topic_list(request):

    if request.method == 'GET':
        topics = UserTopic.objects.all()
        serializer = UserTopicSerializer(topics, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserTopicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201,safe=False)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):
    """
    Retrieve, update or delete a code topic.
    """
    try:
        topic = UserTopic.objects.get(pk=pk)
    except topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserTopicSerializer(topic)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'PUT':
        serializer = UserTopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




