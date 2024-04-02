from django.urls import path
from product import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:id>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('products/reviews/', views.ProductsWithReviews.as_view(), name='products-with-reviews'),
]
