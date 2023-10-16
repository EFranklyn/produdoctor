from django.core.validators import MinValueValidator
from suppliers.models.supplier import Supplier
from .product import Product
from .time_mixin import TimesMixin
from django.db import models

class ProductCatalog(TimesMixin, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f'{self.supplier.name} {self.product.name}'

    class Meta:
        unique_together = ('product', 'supplier')