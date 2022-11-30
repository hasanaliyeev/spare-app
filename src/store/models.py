from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='child', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    count = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ProductIn(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_in')
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    count = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ProductOut(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_out')
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    count = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
