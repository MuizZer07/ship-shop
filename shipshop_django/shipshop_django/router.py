from product.api.viewsets import ProductViewSet
from rest_framework import routers
from users.api.viewsets import UserListView

router = routers.DefaultRouter()
router.register('products', ProductViewSet, base_name='product')
router.register('users', UserListView)

# import requests
#
# url = 'http://127.0.0.1:8000/hello/'
# headers = {'Authorization': 'Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'}
# r = requests.get(url, headers=headers)
