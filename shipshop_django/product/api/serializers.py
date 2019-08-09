from rest_framework import serializers
from product.models import Product, Category

'''
    serializer classes
'''

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields =  '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
