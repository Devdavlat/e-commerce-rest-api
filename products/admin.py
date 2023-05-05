from django.contrib import admin
from .models.category import Category
from .models.product import Product


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# admin.site.register(Product)
admin.site.register(Category)
