from rest_framework import serializers
from suppliers.models.supplier import Supplier
from django_cpf_cnpj.validators import validate_cnpj

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

    cnpj = serializers.CharField(validators=[validate_cnpj])