from product.models import Product
from .serializers import ProductSerializer, OrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from product.models import Product, Order

'''
    model class viewsets for API calls extending
    'ModelViewSet' class which predifines API CRUD operations
'''

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
