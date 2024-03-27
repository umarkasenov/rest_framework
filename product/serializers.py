from rest_framework import serializers
from .models import Category, Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'products']


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = 'id title description price category reviews'.split()
        # depth = 1


class CategoryValidateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, min_length=1)
    category_id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = '__all__'


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, min_length=3)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    product_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


STARS = [
    (star, star * "*") for star in range(1, 6)
]


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500, min_length=1)
    stars = serializers.ChoiceField(choices=STARS, required=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

