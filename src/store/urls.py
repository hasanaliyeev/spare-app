from django.urls import path

from store import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='create_category'),
    path('products/add/', views.create_product, name='create_product'),
    path('products/update/<int:pk>/', views.product_add, name='product_add'),
    path('products/update/', views.product_add, name='product_add'),
    path('products/', views.products, name='products'),
    path('products/detail/<int:pk>/', views.detail, name='detail'),
]
