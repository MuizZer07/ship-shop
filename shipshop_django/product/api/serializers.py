from rest_framework import serializers
from product.models import Product, Order

'''
    serializer classes
'''

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields =  '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields =  '__all__'
