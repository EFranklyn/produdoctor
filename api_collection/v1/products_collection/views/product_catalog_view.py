from rest_framework import viewsets, status
from products.models.product_catalog import ProductCatalog
from ..serializers.product_catalog_serializers import ProductCatalogWriteSerializer, ProductCatalogReadSerializer
from rest_framework.response import Response
class ProductCatalogViewSet(viewsets.ModelViewSet):
    queryset = ProductCatalog.objects.all()
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductCatalogWriteSerializer
        return ProductCatalogReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        read_serializer = ProductCatalogReadSerializer(serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        instance = serializer.instance
        read_serializer = ProductCatalogReadSerializer(instance)
        return Response(read_serializer.data, status=status.HTTP_200_OK)