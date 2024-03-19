from django.urls import path
from product.views import CategoryList, CategoryDetail, ProductList, ProductDetail, ReviewList, ReviewDetail, ProductsWithReviews
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/categories/', CategoryList.as_view(), name='category-list'),
    path('api/v1/categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('api/v1/products/', ProductList.as_view(), name='product-list'),
    path('api/v1/products/reviews/', ProductsWithReviews.as_view(), name='products_with_reviews'),
    path('api/v1/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/v1/reviews/', ReviewList.as_view(), name='review-list'),
    path('api/v1/reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
