from django.contrib import admin
from product.models import Product, Review, Category


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
