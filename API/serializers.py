from rest_framework import serializers
from category.models import  Category,Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title","image","last_updated")


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("title","image","price","category")

