from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from inventory.models import Category
from .serializers import InventoryCategorySerializer

# Create your views here.
# class InventoryCategoryModelViewSet(ModelViewSet):
#     queryset = Category.objects.all() # Fetch all categories
#     serializer_class = InventoryCategorySerializer # Use the serializer

class InventoryCategoryViewSet(ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = InventoryCategorySerializer(queryset, many=True)
        return Response(serializer.data)