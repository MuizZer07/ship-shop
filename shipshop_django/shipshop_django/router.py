from product.api.viewsets import ProductViewSet, OrderViewSet
from rest_framework import routers
from users.api.viewsets import UserListView

router = routers.DefaultRouter()
router.register('products', ProductViewSet, base_name='product')
router.register('users', UserListView)
router.register('orders', OrderViewSet)
