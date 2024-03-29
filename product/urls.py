from django.urls import path
from product import views

urlpatterns = [
    path('categories/', views.CategoryList, name='category-list'),
    path('categories/<int:id>/', views.CategoryDetail, name='category-detail'),
    path('products/', views.ProductList, name='product-list'),
    path('products/<int:id>/', views.ProductDetail, name='product-detail'),
    path('reviews/', views.ReviewList, name='review-list'),
    path('reviews/<int:id>/', views.ReviewDetail, name='review-detail'),
    path('products/reviews/', views.ProductsWithReviews, name='products-with-reviews'),
]
