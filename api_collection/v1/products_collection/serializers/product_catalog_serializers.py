from rest_framework import serializers
from products.models.product_catalog import ProductCatalog

# class ProductCatalogSerializer(serializers.ModelSerializer):
#
#     @staticmethod
#     def validate(data):
#         product = data.get('product')
#         supplier = data.get('supplier')
#         existing_record = ProductCatalog.objects.filter(product=product, supplier=supplier).first()
#         if existing_record:
#             raise serializers.ValidationError("Já existe um registro para este produto e fornecedor.")
#
#         return data
#
#     class Meta:
#         model = ProductCatalog
#         fields = '__all__'

class ProductCatalogWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatalog
        fields = '__all__'

    @staticmethod
    def validate_price(price):
        if price == 0:
            raise serializers.ValidationError("The price of the product cannot be zero")
        return price
class ProductCatalogReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatalog
        fields = '__all__'
        depth = 1
