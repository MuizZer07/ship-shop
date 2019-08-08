from rest_framework import serializers
from product.models import Product, Category

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description', 'available_quantity', 'price', 'image', 'category_id')

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
