from django.db import models

# Create your models here.
class TimesMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, null=True,verbose_name='Data Modificação')

    class Meta:
        abstract = True


class Supplier(TimesMixin, models.Model):
    name = models.CharField(max_length=200)
    legal_name = models.CharField(max_length=200)
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=18, unique=True)
    contact_numbers = models.TextField()

    def __str__(self):
        return self.name