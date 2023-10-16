# Generated by Django 4.2.6 on 2023-10-14 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
        ('products', '0005_alter_productcatalog_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterUniqueTogether(
            name='productcatalog',
            unique_together={('product', 'supplier')},
        ),
    ]