from django.urls import path
from products.views import get_product_list, category, get_product_detail

urlpatterns = [
    path('categories/', category, name='product-category'),
    path('', category, name='product-list'),
    path('<slug:slug>/', get_product_detail, name='product-detail'),
]
