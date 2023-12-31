# Generated by Django 4.2.6 on 2023-10-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Data Modificação')),
                ('name', models.CharField(max_length=200)),
                ('legal_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('zip_code', models.CharField(max_length=10)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('contact_numbers', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
