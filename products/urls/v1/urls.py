from django.urls import path, include
from rest_framework import routers
from api_collection.v1.products_collection.views.category_view import CategoryViewSet
from api_collection.v1.products_collection.views.product_view import ProductViewSet
from api_collection.v1.products_collection.views.product_catalog_view import ProductCatalogViewSet

app_name = 'products'
api_version = 'v1/'
routers = routers.DefaultRouter()
routers.register('categories', CategoryViewSet, basename='categories')
routers.register('products', ProductViewSet, basename='products')
routers.register('products-catalog', ProductCatalogViewSet, basename='products-catalog')

urlpatterns = [
    path(api_version, include(routers.urls), name='products'),
    ]