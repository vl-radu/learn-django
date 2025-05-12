from rest_framework.routers import DefaultRouter
from .views import InventoryCategoryViewSet

router = DefaultRouter()
router.register(r'inventory-category', InventoryCategoryViewSet, basename="inventory-category")

urlpatterns = router.urls