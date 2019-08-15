from rest_framework import generics
from rest_framework import viewsets
from users.models import User
from .serializers import UserSerializer

'''
    viewsets for User serializer
'''

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
