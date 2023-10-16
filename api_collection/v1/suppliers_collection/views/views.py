from rest_framework import viewsets
from suppliers.models.supplier import Supplier
from api_collection.v1.suppliers_collection.serializers.suppliers_serializers import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer