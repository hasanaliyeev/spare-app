from django.contrib import admin

from store.models import Category, Product, ProductOut, ProductIn


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'created', 'updated', 'description', 'count']


@admin.register(ProductIn)
class ProductInAdmin(admin.ModelAdmin):
    list_display = ['product', 'count', 'created']


@admin.register(ProductOut)
class ProductOutAdmin(admin.ModelAdmin):
    list_display = ['product', 'count']


