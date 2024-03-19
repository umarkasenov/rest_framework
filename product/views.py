from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from django.db.models import Avg, Count


class ProductsWithReviews(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        products_data = []
        for product in queryset:
            reviews = Review.objects.filter(product=product)
            reviews_serializer = ReviewSerializer(reviews, many=True)
            average_rating = reviews.aggregate(Avg('stars'))['stars__avg'] if reviews.exists() else None
            product_serializer = self.serializer_class(product)
            products_data.append({
                'product': product_serializer.data,
                'reviews': reviews_serializer.data,
                'average_rating': average_rating
            })
        return Response(products_data)



class CategoryList(generics.ListAPIView):
    queryset = Category.objects.annotate(products_count=Count('products'))
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
