from django.db import models

# Create your models here.
class TimesMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, null=True,verbose_name='Data Modificação')

    class Meta:
        abstract = True
