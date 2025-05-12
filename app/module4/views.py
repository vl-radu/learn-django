from rest_framework.viewsets import (
    # ModelViewSet, 
    ViewSet
)
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import (
    extend_schema,
)
from inventory.models import Category, User
from .serializers import (
    CategorySerializer, 
    CategoryReturnSerializer,
    UserSerializer,
    UserReturnSerializer
)

# Create your views here.
# class InventoryCategoryModelViewSet(ModelViewSet):
#     queryset = Category.objects.all() # Fetch all categories
#     serializer_class = InventoryCategorySerializer # Use the serializer

# class InventoryCategoryViewSet(ViewSet):
#     def list(self, request):
#         queryset = Category.objects.all()
#         serializer = InventoryCategorySerializer(queryset, many=True)
#         return Response(serializer.data)

# Inserting data with create()
class CategoryInsertViewSet(ViewSet):
    @extend_schema(
            request=CategorySerializer, # This links the serializer for the request body
            responses={
                201: CategoryReturnSerializer
            }, # Expected response will be the created category
            tags=["Module 4"],
    )
    def create(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            category_instance = serializer.save()
            return_serializer = CategoryReturnSerializer(category_instance)
            return Response(return_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserInsertViewSet(ViewSet):
    @extend_schema(
        request=UserSerializer,
        responses={
            201: UserReturnSerializer
        },
        tags=["Module 4"],
    )
    def create(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            category_instance = serializer.save()
            return_serializer = UserReturnSerializer(category_instance)
            return Response(return_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Bulk Insert with bulk_create()

class CategoryBulkInsertViewSet(ViewSet):
    @extend_schema(
        request=CategorySerializer(many=True), # Accepts multiple objects
        responses={
            201: CategoryReturnSerializer(many=True) #Returns multiple inserted objects
            }, # Expected response will be the created category
            tags=["Module 4"],
    )
    def create(self, request):
        # Ensure request contains a list of items
        if not isinstance(request.data, list):
            return Response(
                {"error": "Expected a list of objects"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        # Deserialize data (many=True allows multiple objects)
        serializer = CategorySerializer(data=request.data, many=True)

        if serializer.is_valid():
            # Convert validated data to model instances (without saving yet)
            categories = [Category(**item) for item in serializer.validated_data]

            # Use bulk_create() to insert all at once
            created_categories = Category.objects.bulk_create(categories)

            # Serialize the created objects and return response
            return Response(
                CategorySerializer(created_categories, many=True).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)