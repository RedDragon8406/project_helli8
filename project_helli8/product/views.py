

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import UserProduct
from product.serializers import UserProductSerializer
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        products = UserProduct.objects.all()
        serializer = UserProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201,safe=False)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code product.
    """
    try:
        product = UserProduct.objects.get(pk=pk)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class search(APIView):
    def get(self, request, format=None):
        print(request.GET)
        query = request.GET.get('q')
        global title
        title = query
        if query is not None:
            print("shalam")
            result = UserProduct.objects.search(query)
        else:
            result = UserProduct.objects.get_active_products(query)
        serializer = UserProductSerializer(result, many=True)
        return JsonResponse(serializer.data,safe=False)

