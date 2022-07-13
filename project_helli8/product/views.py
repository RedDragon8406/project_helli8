# from rest_framework import filters
# from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from product.models import UserProduct
# from product import serializers
# from django.views.generic import ListView
# from rest_framework.response import Response
# # Create your views here.
#
#
# # class UserProductViewSet(viewsets.ModelViewSet):
# #     """Handle creating, creating and updating profiles"""
# #     serializer_class = serializers.UserProductSerializer
# #     queryset = models.UserProduct.objects.all()
# #     filter_backends = (filters.SearchFilter,)
# #     search_fields = ('name', 'author')
#
#
#
#
# class SearchProductsView(ListView):
#     paginate_by = 3
#
#     def get_queryset(self):
#         request = self.request
#         print(request.GET)
#         query = request.GET.get('q')
#         global title
#         title = query
#         if query is not None:
#             return models.UserProduct.objects.search(query)
#         return models.UserProduct.objects.get_active_products()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = title
#         return context











from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import UserProduct
from product.serializers import UserProductSerializer
from django.http import HttpResponse, JsonResponse

@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        products = UserProduct.objects.all()
        serializer = UserProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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




