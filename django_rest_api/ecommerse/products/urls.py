from django.contrib import admin
from django.urls import path
from products.views import get_all_products, get_one_product, create_product, edit_products, delete_products, update_product

urlpatterns = [
    path ('save/', create_product),
    path ('read/', get_all_products, name='index'),
    path ('get/<int:id>', get_one_product),
    path ('edit/<int:id>', edit_products),
    path ('delete/<int:id>', delete_products),
    path ('update/<int:id>', update_product),
]
