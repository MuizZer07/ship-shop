from rest_framework import generics
from rest_framework import viewsets
from users.models import Buyer, Seller, User
from .serializers import BuyerSerializer, SellerSerializer, UserSerializer

class BuyerListView(generics.ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class SellerListView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
