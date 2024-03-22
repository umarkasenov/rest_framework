from django.urls import path
from product.views import CategoryList, CategoryDetail, ProductList, ProductDetail, ReviewList, ReviewDetail, ProductsWithReviews
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/categories/', CategoryList, name='category-list'),
    path('api/v1/categories/<int:id>/', CategoryDetail, name='category-detail'),
    path('api/v1/products/', ProductList, name='product-list'),
    path('api/v1/products/reviews/', ProductsWithReviews, name='products_with_reviews'),
    path('api/v1/products/<int:id>/', ProductDetail, name='product-detail'),
    path('api/v1/reviews/', ReviewList, name='review-list'),
    path('api/v1/reviews/<int:id>/', ReviewDetail, name='review-detail'),
]
