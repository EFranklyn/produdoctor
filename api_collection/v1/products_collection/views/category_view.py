from rest_framework import viewsets
from ..serializers.category_serializers import CategorySerializer
from products.models.category import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer