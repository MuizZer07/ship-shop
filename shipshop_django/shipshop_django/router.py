from product.api.viewsets import ProductViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('Categories', CategoryViewSet)
