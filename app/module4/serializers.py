from rest_framework import serializers
from inventory.models import Category, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "parent", "name", "slug", "is_active", "level"]

class CategoryReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

class UserReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]