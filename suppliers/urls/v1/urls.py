"""suppliers_collection app routes"""


from django.urls import path, include
from rest_framework import routers
from api_collection.v1.suppliers_collection.views.views import SupplierViewSet

app_name = 'suppliers'
api_version = 'v1/'
router_recipes = routers.DefaultRouter()
router_recipes.register('suppliers', SupplierViewSet, basename='suppliers')

urlpatterns = [
    path(api_version, include(router_recipes.urls), name='suppliers'),
    ]