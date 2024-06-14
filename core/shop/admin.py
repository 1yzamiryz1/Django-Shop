from django.contrib import admin

from .models import ProductCategoryModel, ProductImageModel, ProductModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ('id', 'title','slug', 'stock', 'status','price', 'discount_percent', 'created_date')


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'created_date')


@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
	list_display = ('id', 'file', 'created_date')
