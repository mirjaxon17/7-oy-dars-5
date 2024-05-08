from django.shortcuts import render
from rest_framework.views import APIView
from category.models import Category,Products
from .serializers import CategorySerializer,ProductsSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CategoryListAPIViewSet(APIView):
    def get(self, request):
        category =Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        permission_classes = [IsAuthenticated]
        authentication_classes = [TokenAuthentication]
        filter_backends = (filters.SearchFilter,)
        search_fields = ('price','product__price',)
class ProductlAPIViewSet(ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title','category__title')




