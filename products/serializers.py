from rest_framework import serializers
from products import models
from users.api.serializers import CustomerSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("title", "image",)


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = ("image",)


class ProductNewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ("title", "price", "discount", "main_image")


class CategoryRetriveSerializer(serializers.ModelSerializer):
    categories = ProductNewSerializer(many=True)

    class Meta:
        model = models.Category
        fields = ("title", "categories")


class CategoryProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("title",)


class ReviewsSerializer(serializers.ModelSerializer):
    user = CustomerSerializer()
    product = ProductNewSerializer()

    class Meta:
        model = models.Review
        fields = ("user", "product", "description")


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategoryProductDetailSerializer(many=True, read_only=True)
    images = ProductGallerySerializer(many=True, read_only=True)
    product = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = (
            "title",
            "description",
            "slug",
            "price",
            "discount",
            "color",
            "width",
            "height",
            "length",
            "weight",
            "quantity",
            "is_new",
            "category",
            "images",
            "product"
        )
