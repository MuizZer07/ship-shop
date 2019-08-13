from rest_framework import serializers
from product.models import Product

'''
    serializer classes
'''

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields =  '__all__'
